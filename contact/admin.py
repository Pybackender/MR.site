from django.contrib import admin
from . models import Contact
from painless.models.actions import ExportMixin, PostableMixin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin,PostableMixin,ExportMixin):
    list_display = ['fristname','lastname', 'email', 'created']
    list_filter = ['created']
    search_fields = ['email']

    actions = ['make_published', 'make_draft',
               'export_as_json', 'export_as_csv']
