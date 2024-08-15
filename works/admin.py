from django.contrib import admin

from works.models import Work

# Register your models here.
@admin.register(Work)
class workadmin(admin.ModelAdmin):
    list_display = ['subject','content','avatar','web_site','author','author_about','author_image','author_position']
    prepopulated_fields = {'slug': ('subject',)}
