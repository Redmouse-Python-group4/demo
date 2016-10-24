from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Article (models.Model):
    title=models.CharField(max_length=100)
    body =models.TextField()
    date_create=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.title, self.date_create)

    def __unicode__(self):
        return "%s %s"%(self.title, self.date_create)