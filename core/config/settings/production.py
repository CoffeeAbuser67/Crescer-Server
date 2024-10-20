from .base import *  # noqa
from .base import env
from .base import DATABASES

# HERE PRODUCTION SETTINGS


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", False)


CORS_ALLOWED_ORIGINS = [
    "https://cresceredesenvolver.com",    
    "https://www.cresceredesenvolver.com",
]

CORS_ALLOW_CREDENTIALS = True


# WARN
ADMINS = [("Henry Melen", "hymelen@hotmail.com")]


# WARN
# TODO add domain names of the production server
CSRF_TRUSTED_ORIGINS = ["https://cresceredensenvolver.com"]



SECRET_KEY = env("DJANGO_SECRET_KEY")

# HERE
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["cresceredesenvolver.com", "www.cresceredesenvolver.com"])


# HERE
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")



SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)



SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True



# TODO: change to 518400 later
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60



SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)


SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)



# # WARN
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# WARN
SITE_NAME = "Crescer Cards"



# ✳ ✦─────────────────────────────────────────────────────────────────────➤
# WARN
# SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)


# EMAIL_SUBJECT_PREFIX = env(
#     "DJANGO_EMAIL_SUBJECT_PREFIX",
#     default="[Authors Haven]",
# )


# EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"

# EMAIL_HOST = "smtp.mailgun.org"
# EMAIL_HOST_USER = "postmaster@mg.trainingwebdev.com"
# EMAIL_HOST_PASSWORD = env("SMTP_MAILGUN_PASSWORD")
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DOMAIN = env("DOMAIN")
# ✳ ✦─────────────────────────────────────────────────────────────────────➤



LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
