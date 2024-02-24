from django.contrib import admin

from .models import Case
from import_export.admin import ImportExportModelAdmin


# # Register your models here.

admin.site.register(Case, ImportExportModelAdmin)
#admin.site.register(State)