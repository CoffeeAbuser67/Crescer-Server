# -*- coding: utf-8 -*-
"""

@author: henry
"""

import os
import django
import sys


print(django.get_version())



# CurrentWorkDirectory = os.getcwd()
# sys.path.append(CurrentWorkDirectory)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local')


# Now set up Django
django.setup()



# Import your models and run your script
from your_app.models import Patient  # Replace 'your_app' with your actual app name


# Your script logic here



