"""
Django settings for arteliasite project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os, logging
import logging.config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "el#4!%-fd*sm(sliyq+p_x+ym+=xovjq+9pl!oizcg1(z6%s29"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "lamiacarto",
    "webpack_loader",
    "rest_framework",
    # "corsheaders",
]


WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "lamiacarto/bundles/",
        # 'STATS_FILE': os.path.join(BASE_DIR, 'pvr', 'static','bundles', 'webpack-stats.json'),
        "STATS_FILE": os.path.join(BASE_DIR, "lamiacarto", "webpack-stats.json"),
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8000",
]

ROOT_URLCONF = "arteliasite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates"),],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "arteliasite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    # {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    # {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    # {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

AUTH_USER_MODEL = "lamiacarto.User"

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.abspath(os.path.join(BASE_DIR, "node_modules")),
    os.path.abspath(os.path.join(BASE_DIR, "..", "Lamia", "worktypeconf")),
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        # "console": {"format": "%(thread)d-%(name)-12s %(levelname)-8s %(message)s"},
        "console": {
            "format": "%(asctime)s :: %(thread)d :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
            "datefmt": "%H:%M:%S",
        },
        "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "console",},
    },
    "loggers": {
        "": {"handlers": ["console"], "level": "DEBUG", "propagate": True,},
        "Lamia.iface.qgscanvas.ifaceqgiscanvas": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
            "formatter": "console",
        },
    },
}

logging.config.dictConfig(LOGGING)
