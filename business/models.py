from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Value(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(null=False, blank=False,default=timezone.now)
    value = models.FloatField()