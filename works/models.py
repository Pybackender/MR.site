from django.db import models

from painless.models.mixins import OrganizedMixin

# Create your models here.


class Work(models.Model):
    subject = models.CharField(max_length=125)
    slug = models.CharField(max_length=125)
    content = models.CharField(max_length=500)
    avatar = models.ImageField(
        upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    web_site = models.URLField(null=True, blank=True)
    author =models.CharField(max_length=125)
    author_about =models.CharField(max_length=225)
    author_image =models.ImageField(null=True,blank=True)
    author_position =models.CharField(max_length=125,null=True,blank=True)

    class Meta:
        verbose_name = ('work')
        verbose_name_plural = ('works')

    def __str__(self):
        return self.subject
