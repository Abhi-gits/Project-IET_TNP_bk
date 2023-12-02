# flake8: noqa

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import ietapp
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

# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),

#     #'default': dj_database_url.parse("DATABASE_URL", conn_max_age=600),
# }

#postgres://placement_user:UJVM2nwSRTyHn6fNCM8BtxlJdh2nf741@dpg-cjbloc3bq8nc73dndb00-a.singapore-postgres.render.com/placement
