from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=125)
    skill = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(max_length=125)

    class Meta:
        verbose_name = ('skill')
        verbose_name_plural = ('skills')

    def __str__(self):
        return self.skill


class About(models.Model):
    title = models.CharField(max_length=125)
    slug = models.CharField(max_length=125)
    content = models.CharField(max_length=500,null=True,blank=True)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    video = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = ('about')
        verbose_name_plural = ('abouts')

    def __str__(self):
        return self.title  # Adjust this to return a valid field
