from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class PublicMediaStorage(S3Boto3Storage):
    location = "lamiia"
    default_acl = "public-read"
    file_overwrite = False
