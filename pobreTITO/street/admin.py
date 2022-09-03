from django.contrib import admin
from street.models import *

# Register your models here.

class StreetAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ["code", "name"]
    ordering = ("code",)

admin.site.register(Street, StreetAdmin)