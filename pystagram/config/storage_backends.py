from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    bucket_name = 'oz-pystagram'
    custom_domain = f'{bucket_name}.s3.amazonaws.com'