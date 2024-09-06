from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
import logging


logger = logging.getLogger(__name__)




# {✪}  CustomUserManager
class CustomUserManager(BaseUserManager):
    

    # (●) email_validator
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_("You must provide a valid email address."))

    # (●) create_user
    def create_user(self, first_name, last_name, email, password, role = 'user', **extra_fields):
    
        logger.info(" ● create_user called") # _LOG_  ● create_user 

        if not first_name:
            raise ValueError(_("Users must have a first name."))
        if not last_name:
            raise ValueError(_("Users must have a last name."))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Users must have an email address."))

        # _PIN_ Set is_staff and is_superuser based on role field

        if role == 'super':
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
        
        elif role == 'admin' or role == 'staff':
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', False)
        
        else:
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)


        user = self.model(
            first_name=first_name, last_name=last_name, email=email, role=role, **extra_fields
        )
        user.set_password(password)


        user.save(using=self._db)
        return user

    
    # (●) create_superuser
    def create_superuser(self, first_name, last_name, email, password, **extra_fields):

        if not password:
            raise ValueError(_("Superuser must have a password."))

        extra_fields.setdefault('role', 'super')

        # _PIN_  This check can't be here anymore

        # if extra_fields.get("is_staff") is not True:
        #     raise ValueError(_("Superuser must have is_staff=True."))

        # if extra_fields.get("is_superuser") is not True:
        #     raise ValueError(_("Superuser must have is_superuser=True."))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Superuser must have an email address."))

        user = self.create_user(first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user
