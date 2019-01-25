import django
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone
import pytz
import geoip2.database
import os

from .signals import detected_timezone
from .utils import get_ip_address_from_request, is_valid_ip, is_local_ip


db_loaded = False
db = None
db_v6 = None


def load_db_settings():
    GEOLITE2_DATABASE = getattr(settings, 'GEOLITE2_DATABASE', 'GeoLite2-City.mmdb')

    if not GEOLITE2_DATABASE:
        raise ImproperlyConfigured("GEOLITE2_DATABASE setting has not been properly defined.")

    if not os.path.exists(GEOLITE2_DATABASE):
        raise ImproperlyConfigured("GEOLITE2_DATABASE setting is defined, but file does not exist.")

    return GEOLITE2_DATABASE


load_db_settings()


def load_db():
    GEOLITE2_DATABASE = load_db_settings()

    global db
    db = db = geoip2.database.Reader(GEOLITE2_DATABASE)

    global db_loaded
    db_loaded = True


def lookup_tz(ip):
    """
    Lookup a timezone for the ip using the v2 database.
    :param ip: the ip address, v4 or v6
    :return:   the timezone
    """
    if not db_loaded:
        load_db()
    #
    # v2 databases support both ipv4 an ipv6
    #
    try:
        response = db.city(ip)
    except geoip2.errors.AddressNotFoundError:
        return None
    return response.location.time_zone


if django.VERSION >= (1, 10):
    from django.utils.deprecation import MiddlewareMixin
    middleware_base_class = MiddlewareMixin
else:
    middleware_base_class = object


class EasyTimezoneMiddleware(middleware_base_class):
    def process_request(self, request):
        """
        If we can get a valid IP from the request,
        look up that address in the database to get the appropriate timezone
        and activate it.

        Else, use the default.

        """

        if not request:
            return

        if not db_loaded:
            load_db()

        tz = request.session.get('django_timezone')

        if not tz:
            # use the default timezone (settings.TIME_ZONE) for localhost
            tz = timezone.get_default_timezone()

            client_ip = get_ip_address_from_request(request)
            ip_addrs = client_ip.split(',')
            for ip in ip_addrs:
                if is_valid_ip(ip) and not is_local_ip(ip):
                    tz = lookup_tz(ip)
                    break

        if tz:
            timezone.activate(tz)
            request.session['django_timezone'] = str(tz)
            if getattr(settings, 'AUTH_USER_MODEL', None) and getattr(request, 'user', None):
                detected_timezone.send(sender=get_user_model(), instance=request.user, timezone=tz)
        else:
            timezone.deactivate()
