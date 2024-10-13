# -*- coding: utf-8 -*-
"""
_PIN_ 🦀 
@author: henry # 
"""
import os
import django
import sys
import logging
logger = logging.getLogger(__name__)


# CurrentWorkDirectory = os.getcwd()
# sys.path.append(CurrentWorkDirectory)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

# Now set up Django
django.setup()

print(django.get_version())
# logger.info(django.get_version())

# Import your models and run your script
from apps.patients.models import Patient  # Replace 'your_app' with your actual app name
all_patients = Patient.objects.all()

print(all_patients.values())

# logger.info('all patients : ', all_patients)

