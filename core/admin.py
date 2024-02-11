from django.contrib import admin

from .models import Case, Contact
from import_export.admin import ImportExportModelAdmin


# # Register your models here.

admin.site.register(Case, ImportExportModelAdmin)
admin.site.register(Contact)
#admin.site.register(State)