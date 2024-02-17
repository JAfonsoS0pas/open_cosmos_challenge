from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(null=False, blank=False,default=timezone.now)
    value = models.FloatField()
    tags = ArrayField(models.CharField(max_length=100), blank=True)