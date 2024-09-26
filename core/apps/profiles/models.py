from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedModel 


# HERE
class Profile(TimeStampedModel):

  parent_name = models.CharField(verbose_name=_("parent name"), blank=True, max_length=150)
  phone_number = PhoneNumberField( 
    verbose_name=_("phone number"), blank=True, max_length=30, default=""
  )   
  note = models.TextField( 
    verbose_name=_("note"), blank=True, default=""
  )
  country = CountryField( 
      verbose_name=_("country"), default="BR", blank=False, null=False
  )
  city = models.CharField( 
      verbose_name=_("city"),
      max_length=180,
      default="Ilhéus",
      blank=False,
      null=False,
  )
  profile_photo = models.ImageField( 
    verbose_name=_("profile photo"), default="/profile_default.png"
  )


