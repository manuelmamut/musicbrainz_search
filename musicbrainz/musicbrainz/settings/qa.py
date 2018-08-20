from .base import *

DEBUG = True

print("QA")

ALLOWED_HOSTS = ['104.131.185.138']

STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

MEDIA_ROOT = STATIC_ROOT + '/media/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 60,
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'

CACHE_MIDDLEWARE_SECONDS = 60

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}