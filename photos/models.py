from django.db import models

from painless.models.mixins import OrganizedMixin

class Photo(OrganizedMixin):
    image = models.ImageField(
        upload_to="image/%Y/%m/%d", null=True, blank=True) 
    
    class Meta:
        verbose_name = ('photo')
        verbose_name_plural = ('photos')

    def __str__(self):
        return self.title