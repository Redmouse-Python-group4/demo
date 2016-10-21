from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Coment(models.Model):
	title=models.CharField(max_length=100)
	body=models.CharField(max_length=100)