
# HERE 
from .base import *
from .base import env

# WARN SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="gJOqMl5WCF5X9fLJX0gHhXYooS-ZcOdGRcvL4mkIjc-dJ4j4fJw",
)

# WARN SECURITY: don't run with debug turned on in production!
DEBUG = True



CSRF_TRUSTED_ORIGINS = [     
    "http://localhost:81",
    "http://127.0.0.1:81"
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:81",
    "http://127.0.0.1:81"
]


# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000"
# ]

CORS_ALLOW_CREDENTIALS = True

