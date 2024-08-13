from django.contrib import admin

from works.models import Work

# Register your models here.
@admin.register(Work)
class workadmin(admin.ModelAdmin):
    list_display = ['title','subject','content','avatar']
    prepopulated_fields = {'slug': ('title',)}
