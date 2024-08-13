from django.db import models
from painless.models.mixins import OrganizedMixin


class About(OrganizedMixin):
    avatar = models.ImageField(
        upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    position = models.CharField(max_length=225, null=True, blank=True)
    position1 = models.CharField(max_length=225, null=True, blank=True)
    position2 = models.CharField(max_length=225, null=True, blank=True)
    position3 = models.CharField(max_length=225, null=True, blank=True)
    position4 = models.CharField(max_length=225, null=True, blank=True)
    position5 = models.CharField(max_length=225, null=True, blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)
    video = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = ('about')
        verbose_name_plural = ('abouts')

    def __str__(self):
        return self.title
