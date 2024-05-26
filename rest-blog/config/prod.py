from .local import *

DEBUG = False

ALLOWED_HOSTS = ['jihyunchoi.pythonanywhere.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
