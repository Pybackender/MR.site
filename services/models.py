from django.db import models

from painless.models.mixins import OrganizedMixin


class Service(OrganizedMixin):
    subject = models.CharField(max_length=125)
    content = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'service'
        verbose_name = 'services'
        get_latest_by = ['-published_at']

    def __str__(self):
        return self.title
    