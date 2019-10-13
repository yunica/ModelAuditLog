from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class AuditModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    create = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)

    class Meta:
        abstract = True


class FirstModel(AuditModel):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=40)
