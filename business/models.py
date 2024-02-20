from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Value(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(null=False, blank=False,default=timezone.now)
    value = models.FloatField()

class DiscardedValue(Value):
    reasons = ArrayField(models.CharField(max_length=100))

    class Meta:
        verbose_name_plural = "Discarded Data"

    def __str__(self):
        return f"Discarded data for {self.reasons}"