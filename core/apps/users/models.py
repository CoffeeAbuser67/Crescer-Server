import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager
import logging


logger = logging.getLogger(__name__)


# {✪} User ↯
class User(AbstractBaseUser, PermissionsMixin):

    logger.info("I'm being called bruh. ") # _LOG_ ● User
    ROLES = (
        ('super', 'Superuser'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    )


    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_("first name"), max_length=50)
    last_name = models.CharField(verbose_name=_("last name"), max_length=50)
    email = models.EmailField(
        verbose_name=_("email address"), db_index=True, unique=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("profile photo"), default="/user_default.png"
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    role = models.CharField(max_length=10, choices=ROLES, default='user')
    
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    # {□} CustomUserManager
    objects = CustomUserManager() 

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.first_name

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    @property
    def get_short_name(self):
        return self.first_name
