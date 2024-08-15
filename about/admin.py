from django.contrib import admin
from .models import About, Skill
# Register your models here.


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("skill",)}  # Update to match Skill model
    list_display = ('title','skill', 'slug')


@admin.register(About)
class Aboutadmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'avatar', 'video']
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_header = "MR"
admin.site.site_title = "حسن سایت ادمین"
admin.site.index_title = "خوش امدی حسن "
