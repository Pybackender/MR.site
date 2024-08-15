from django.utils import timezone
from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(
        upload_to="image/%Y/%m/%d", null=True, blank=True) 
    published_at =models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = ('photo')
        verbose_name_plural = ('photos')

    def __str__(self):
        return self.title