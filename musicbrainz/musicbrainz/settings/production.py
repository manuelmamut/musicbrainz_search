from .base import *

DEBUG = False

print('production')
ALLOWED_HOST = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#STATIC_ROOT = MUST BE A FOLDER IN YOUR SERVING FILES SERVER

#MEDIA_ROOT = STATIC_ROOT + '/media/'
