from django.db import models
from painless.models.mixins import OrganizedMixin


class Service(models.Model):
    subject = models.CharField(max_length=125)
    slug = models.CharField(max_length=125)
    youtube = models.URLField(null=True, blank=True)
    content = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        ordering = ['subject']
        verbose_name_plural = 'service'
        verbose_name = 'services'
        get_latest_by = ['-published_at']

    def __str__(self):
        return self.subject
    