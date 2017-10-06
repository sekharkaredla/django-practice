from __future__ import unicode_literals

from django.db import models

from django.conf import settings
# Create your models here.


class Post(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=200)
    likes = models.IntegerField(default=0,null=False)
    private = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)


    class Meta:
        unique_together = (('image','owner'))

    def __str__(self):
        return self.caption
