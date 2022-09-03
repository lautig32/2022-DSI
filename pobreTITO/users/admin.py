from django.contrib import admin

from django.contrib.auth.models import Group, User
from django.db.models import Q

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'cuil_cuim', 'email',)
    list_display_minimum = ('last_name', 'first_name', 'cuil_cuim',)
    search_fields = ['cuil_cuim', 'first_name', 'last_name', 'email', ]
    ordering = ('-is_active', 'last_name', 'first_name', )
    fields = ('username', ('email', 'password',), ('last_name', 'first_name',),'cuil_cuim',('mobile', 'phone',),
                ('is_active', 'is_staff', 'is_superuser',),
              'description')

    def save_model(self, request, obj, form, change):
        # obj.is_staff = obj.user_type != Person.SUBSCRIBE

        if 'password' in form.changed_data:
            obj.set_password(obj.password)
        obj.save()


admin.site.register(User, UserAdmin)
