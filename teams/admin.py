from django.contrib import admin

from teams.models import Team

# Register your models here.
@admin.register(Team)
class teamadmin(admin.ModelAdmin):
    list_display =['name','positions','content','email','image','instagram','github','linkedin']
    prepopulated_fields = {'slug': ('name',)}