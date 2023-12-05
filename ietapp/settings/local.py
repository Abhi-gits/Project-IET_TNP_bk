# flake8: noqa

from .base import *

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#         'default': {
#             'ENGINE': config('MONGO_ENGINE'), 
#             'NAME': config('MONGO_DATABASE'),
#             'ENFORCE_SCHEMA': False,
#             'CLIENT': {
                
#                 'host': config('MONGO_HOST'),
#             }  
#         }
# }