from django.db import models
from django.core.validators import validate_email
from painless.models.mixins import TimeStampedMixin


class Contact(TimeStampedMixin):
    fristname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(
                              validators=[validate_email])
    message = models.TextField()

    class Meta:
        ordering = ['-created']
        verbose_name = "contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.email
