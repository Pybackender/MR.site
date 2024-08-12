from django.contrib import admin
from .models import About
# Register your models here.
@admin.register(About)
class Aboutadmin(admin.ModelAdmin):
    list_display = ['title','slug','content','avatar','position']

admin.site.site_header = "MR"
admin.site.site_title = "حسن سایت ادمین"
admin.site.index_title = "خوش امدی حسن "    