from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.common.models import TimeStampedModel 


# {✪} Patient
class Patient(TimeStampedModel):

  patient_name = models.CharField(verbose_name=_("patient name"), max_length=45)
  parent_name = models.CharField(verbose_name=_("parent name"), max_length=45)

  phone_number = models.CharField( 
    verbose_name=_("phone number"), max_length=30, blank=True, default=""
  )   

  email = models.EmailField(
      verbose_name=_("email address"), db_index=True, unique=True, blank=True
  )

  note = models.TextField( 
    verbose_name=_("note"), blank=True, default=""
  )


  country = CountryField( 
      verbose_name=_("country"), default="", blank=True, null=False
  )


  city = models.CharField( 
      verbose_name=_("city"),
      max_length=180,
      default="",
      blank=True,
      null=False,
  )
  
  # # WARN I don't know how to save image yet
  # profile_photo = models.ImageField( 
  #   verbose_name=_("profile photo"), default="/profile_default.png", blank=True, null=True,
  # )

  birth_date = models.DateField()

  expiration_date = models.DateField()
