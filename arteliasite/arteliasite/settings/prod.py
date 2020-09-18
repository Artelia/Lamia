"""
Django settings for arteliasite project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from .default import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "el#4!%-fd*sm(sliyq+p_x+ym+=xovjq+9pl!oizcg1(z6%s29"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Application definition

# WEBPACK_LOADER = {
#     "DEFAULT": {
#         "BUNDLE_DIR_NAME": "lamiacarto/prod/",
#         # "BUNDLE_DIR_NAME": "dist/",
#         # 'STATS_FILE': os.path.join(BASE_DIR, 'pvr', 'static','bundles', 'webpack-stats.json'),
#         "STATS_FILE": os.path.join(BASE_DIR, "lamiacarto", "webpack-stats-prod.json"),
#     }
# }

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

CORS_ORIGIN_WHITELIST = ["http://127.0.0.1:8000", "localhost"]

ROOT_URLCONF = "arteliasite.urls"


WSGI_APPLICATION = "arteliasite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "lamiaunittest",
        "USER": "pvr",
        "PASSWORD": "pvr",
        "HOST": "docker.for.win.localhost",
        # "HOST": "host.docker.internal",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    # os.path.abspath(os.path.join(BASE_DIR, "node_modules")),  # for bootstrap
    ("forms", os.path.abspath(os.path.join(BASE_DIR, "..", "Lamia", "worktypeconf"))),
    ("img", os.path.join(BASE_DIR, "lamiacarto", "static", "assets", "img")),
]

STATIC_ROOT = "/static/"

MEDIA_ROOT = os.path.join("C:/", "media")
MEDIA_URL = "/media/"

