from unittest.util import _MAX_LENGTH
from xml.sax.handler import feature_external_ges
from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=True, null=True)
    featured    = models.BooleanField(default=False)