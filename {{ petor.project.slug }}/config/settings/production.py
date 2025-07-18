from .base import *

DEBUG = False

ALLOWED_HOSTS = []

CORS_ALLOWD_ORIGINS = []
CORS_ALLOWD_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOWD_HEADERS = ['*']
CORS_ALLOW_CREDENTIALS = True

# AWS S3 setup
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": "media",
            "file_overwrite": False,
            "object_parameters": {
                "CacheControl": "max-age=86400",
            },
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": "static",
        },
    },
}

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
AWS_S3_CUSTOM_DOMAIN = f's3.{AWS_S3_REGION_NAME}.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}'
AWS_QUERYSTRING_AUTH = False  # Don't add complex authentication-related query parameters for URLs
AWS_S3_FILE_OVERWRITE = False  # Don't overwrite files with the same name

COLLECTFASTA_STRATEGY = 'collectfasta.strategies.boto3.Boto3Strategy'
