# your_app/signals.py

import logging

from django.apps import apps

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from django.contrib.auth.models import Group


logger = logging.getLogger(__name__)

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    Group = apps.get_model('auth', 'Group')
    roles = ['super', 'admin', 'staff', 'user']
    logger.info("post_migrate signal received.") # [LOG] signal 
    for role in roles:
        Group.objects.get_or_create(name=role)
    

    