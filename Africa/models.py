
from django.db import models

# Create your models here.
class Community(models.Model):
    community_id = models.IntegerField(max_length=200)
    title = models.CharField(max_length=200)
    champions = models.CharField(max_length=250)

