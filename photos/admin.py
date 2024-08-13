from django.contrib import admin

from photos.models import Photo

# Register your models here.
@admin.register(Photo)
class photoadmin(admin.ModelAdmin):
    list_display = ['title','image','published_at']
    prepopulated_fields = {'slug': ('title',)}