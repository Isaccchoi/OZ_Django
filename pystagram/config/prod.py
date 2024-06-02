from .base import *

DEBUG = False

ALLOWED_HOSTS = ['3.36.114.50', 'oz.isaccchoi.com',]

INSTALLED_APPS += ['storages']

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

AWS_ACCESS_KEY_ID = SECRET['S3']['key']
AWS_SECRET_ACCESS_KEY = SECRET['S3']['secret']
AWS_STORAGE_BUCKET_NAME = SECRET['S3']['name']

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'config.storage_backends.MediaStorage'
