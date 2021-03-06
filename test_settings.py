import django


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
SECRET_KEY = "secret_key_for_testing"
INSTALLED_APPS = ['django.contrib.auth', 'django.contrib.sites', 'django.contrib.sessions', 'django.contrib.contenttypes', 'easy_timezones']
GEOLITE2_DATABASE = 'GeoLite2-City.mmdb'
ROOT_URLCONF = 'easy_timezones.urls'
TIME_ZONE = 'UTC'
ALLOWED_HOSTS = ["*"]
DEBUG = True

AUTH_USER_MODEL = 'auth.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# use new MIDDLEWARE introduced in 1.10
MIDDLEWARE = ['django.contrib.sessions.middleware.SessionMiddleware', 'easy_timezones.middleware.EasyTimezoneMiddleware']
