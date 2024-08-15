from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=125)
    slug = models.CharField(max_length=125)
    positions = models.CharField(max_length=125)
    content = models.CharField(max_length=500)
    email = models.EmailField(null=True,blank= True)
    image = models.ImageField()
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'team'
        verbose_name = 'teams'
        get_latest_by = ['-published_at']

    def __str__(self):
        return self.name