from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db.models import Sum


class Article (models.Model):
    title=models.CharField(max_length=100)
    body =models.TextField()
    date_create=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey('Category')

    def __str__(self):
        return "%s %s" % (self.title, self.date_create)

    def __unicode__(self):
        return "%s %s"%(self.title, self.date_create)

    def get_rating(self):
        rating = Reting.objects.filter(article=self).aggregate(sum_mark=Sum('mark'))
        return rating['sum_mark'] if rating['sum_mark'] is not None else 0
    get_rating.short_description="Rating"


class Category(models.Model):
    parenth = models.ForeignKey('self', blank=True, null=True, default=None)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s(%s)"%(self.name, self.slug)


class Comment(models.Model):
    body = models.TextField()
    article_id = models.ForeignKey(Article)
    enable = models.BooleanField(default=False)
    author = models.ForeignKey(User, blank=True, null=True, default=None)

    def __str__(self):
        return "Comments to %s"%self.article_id.title

class Reting(models.Model):
    MARK =(
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    article=models.ForeignKey(Article, related_name='rating')
    mark = models.PositiveSmallIntegerField(choices=MARK)