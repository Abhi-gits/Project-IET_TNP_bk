# flake8: noqa

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import mongoengine
from .base import *

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

sentry_sdk.init(
    dsn=config("SENTRY_DSN", default=""),
    environment=SIMPLE_ENVIRONMENT,
    release="ietapp@%s" % ietapp.__version__,
    integrations=[DjangoIntegration()],
)


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================


DATABASES = {
        'default': {
            'ENGINE': os.getenv('MONGO_ENGINE'),
            'NAME': os.getenv('MONGO_DATABASE'),
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                
                'host': os.getenv('MONGO_HOST')
            }  
        }
}
