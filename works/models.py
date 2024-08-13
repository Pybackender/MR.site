from django.db import models

from painless.models.mixins import OrganizedMixin

# Create your models here.
class Work(OrganizedMixin):
    subject = models.CharField(max_length=125)
    content = models.CharField(max_length=500)
    avatar = models.ImageField(
        upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    
    class Meta:
        verbose_name = ('work')
        verbose_name_plural = ('works')

    def __str__(self):
        return self.title
    