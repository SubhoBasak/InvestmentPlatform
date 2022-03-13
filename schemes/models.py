from operator import mod
from statistics import mode
from django.db import models


class schemeModel(models.Model):
    title = models.CharField(
        max_length=255, default='', null=False, blank=False)
    description = models.TextField(null=True, blank=True)
