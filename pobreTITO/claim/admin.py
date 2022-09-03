from django.contrib import admin

# Register your models here.

from claim.models import *
from users.models import User

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "is_active")
    search_fields = ["name"]
    list_filter = ("is_active",)
    ordering = ("name",)

class ReasonAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "description", "is_active")
    search_fields = ["name", "type__name"]
    list_filter = ("type", "is_active",)
    autocomplete_fields = ('type',)
    ordering = ("type",)


class ClaimRegisterAdmin(admin.ModelAdmin):
    list_display = ("id", "reason", "date_register_claim", "date_modified_claim", "reception", "state_local",'street_location',)
    fields_extras = (('number_phone','reception'),('reason', 'state_local'), ("street_location", "number_street"), ("street_location_a", "street_location_b"),
                    "citizen",("date_register_claim", "date_modified_claim"), "description",'user_last_change',)
    readonly_fields = ("date_register_claim", "date_modified_claim",'user_last_change',)
    search_fields = ("id", "reason__name", "reason__type__name", 'state_local', 'reception', 'street_location__name',)
    list_filter = ("state_local", 'reception', "reason__type", "reason", "street_location",)
    autocomplete_fields = ('reason', 'street_location', 'street_location_a', 'street_location_b', 'citizen',)


admin.site.register(Type, TypeAdmin)

admin.site.register(Reason, ReasonAdmin)

admin.site.register(ClaimRegister, ClaimRegisterAdmin)