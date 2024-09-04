from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ApiTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api_test'
    verbose_name = _("API Testes")