from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from uuid import uuid1


class Auditor(models.Model):
    """
   content_object = object name
    object_id = object id
    field = field change
    action = create , delete, update
    old_value , new_value = values in question
    stamp = date create
    user_name = username user in session
    user_id = username user in session
    content_type = name of model (Contentype model )

    """
    id = models.UUIDField(default=uuid1, primary_key=True)
    content_object = models.TextField()
    object_id = models.CharField(max_length=255, blank=True)
    field = models.CharField(max_length=255, blank=True)
    action = models.CharField(max_length=20)
    old_value = models.TextField(blank=True, default='')
    new_value = models.TextField(blank=True, default='')
    stamp = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, blank=True, on_delete=models.PROTECT)

    if 'tenant' in settings.AUDITOR:
        tenant = models.ForeignKey(settings.AUDITOR['tenant'])

