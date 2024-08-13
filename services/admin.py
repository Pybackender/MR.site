from django.contrib import admin
from services.models import Service

# Register your models here.
@admin.register(Service)
class serviceadmin(admin.ModelAdmin):
    list_display = ['title', 'subject','content']
    prepopulated_fields = {'slug': ('title',)}