![Timezones. Yuck.](http://i.imgur.com/Qc2W47H.gif)

django-easy-timezones-redux [![Build Status](https://travis-ci.org/maurizi/django-easy-timezones.svg)](https://travis-ci.org/maurizi/django-easy-timezones)
=====================

Easy IP-based timezones for Django (>=1.11) based on MaxMind GeoIP, with IPv6 support.
Updated fork of [`django-easy-timezones`](https://github.com/Miserlou/django-easy-timezones) that uses the new version of MaxMind's GeoIP2 database.

Quick start
-----------

1. Install django-easy-timezones-redux

    ```python
    pip install django-easy-timezones-redux
    ```

1. Add "easy-timezones" to your INSTALLED_APPS setting like this:

    ```python
    INSTALLED_APPS = (
      ...
      'easy_timezones',
    )
    ```

1. Add EasyTimezoneMiddleware to your MIDDLEWARE

    ```python
    MIDDLEWARE = (
      ...
      'easy_timezones.middleware.EasyTimezoneMiddleware',
    )
    ```

1. Add a path to the [MaxMind GeoLite2 cities databases](https://dev.maxmind.com/geoip/geoip2/geolite2/) in your settings file:

    ```python
    GEOIP2_DATABASE = '/path/to/your/geoip/database/GeoLite2-City.mmdb'
    ```

1. Enable localtime in your templates.

    ```python
    {% load tz %}
        The UTC time is {{ object.date }}
    {% localtime on %}
        The local time is {{ object.date }}
    {% endlocaltime %}
    ```
1. That's it!

## Signals

You can also use signals to perform actions based on the timezone detection.

1. To hook into the Timezone detection event to, say, save it to the request's user somewhere more permanent than a session, do something like this:

	```python
	from easy_timezones.signals import detected_timezone	

	@receiver(detected_timezone, sender=MyUserModel)
	def process_timezone(sender, instance, timezone, **kwargs):
    	if instance.timezone != timezone:
        	instance.timezone = timezone
        	instance.save()
	```
