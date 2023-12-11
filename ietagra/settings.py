from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECRET_KEY = "django-insecure-w+*dsp-w_l8hs@_28q&b)km7dpyw=og@qq9q16vp$hk30wa_x%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # API app for REST API
    "api",
    # our all apps
    "api.basic",
    "api.account",
    # "api.tnp",
    "api.placement",
    "api.batch",
    "api.course",
    # Third party apps
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    'drf_spectacular',
]

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "ietagra.urls"

INTERNAL_IPS = ["127.0.0.1"]

WSGI_APPLICATION = "ietagra.wsgi.application"

AUTH_USER_MODEL = "account.User"


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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


# ==============================================================================
# REST FRAMEWORK SETTINGS
# ==============================================================================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

PASSWORD_RESET_TIMEOUT = 1200  # 1200 Sec = 20 Min


INTERNAL_IPS = ["127.0.0.1"]

# CORS_ALLOWED_ORIGINS = ['*']
CORS_ALLOW_ALL_ORIGINS = True


# JWT Settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
}


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

# Email Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")
EMAIL_USE_TLS = True

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.environ.get("DBNAME"),
#         "HOST": os.environ.get("DBHOST"),
#         "USER": os.environ.get("DBUSER"),
#         "PASSWORD": os.environ.get("DBPASS"),
#         'PORT': os.environ.get("DBPORT"),
#         "OPTIONS": {"sslmode": "require"},
#     }
# }

DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'IETAGRATNP',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': os.environ.get("DBMONGO"),
            }  
        }
}

# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
# }



# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]



# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

# When using the console backend, the email will be printed to the console instead of being sent through the network.
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



# ==============================================================================
# Azure settings
# ==============================================================================

# DEFAULT_FILE_STORAGE = "ietagra.azure_storage.AzureMediaStorage"
# STATICFILES_STORAGE = "ietagra.azure_storage.AzureStaticStorage"

# AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
# AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")
# AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"

# STATIC_URL = f"https://{AZURE_CUSTOM_DOMAIN}/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/media/"
# MEDIA_ROOT = BASE_DIR / "mediafiles"

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "staticfiles"



# ==============================================================================
# API Documentation settings
# ==============================================================================

SPECTACULAR_SETTINGS = {
    'TITLE': 'IETAGRA API',
    'DESCRIPTION': 'API for IETAGRA',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
    },
    # OTHER SETTINGS
}

# ==============================================================================