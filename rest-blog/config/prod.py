from .local import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1:8000']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
