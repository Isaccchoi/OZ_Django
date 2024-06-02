from .base import *
DEBUG = True

ALLOWED_HOSTS = ['3.36.114.50', 'oz.isaccchoi.com',]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": SECRET['db']['name'],
        "USER": SECRET['db']['user'],
        "PASSWORD": SECRET['db']['password'],
        "HOST": SECRET['db']['host'],
        "PORT": "5432"
    }
}
