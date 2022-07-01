from django.contrib import admin

from django.contrib.auth.models import Group, User
from django.db.models import Q

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'cuil_cuim', 'email', 'user_type', 'profile_picture_short_tag', )
    list_display_minimum = ('last_name', 'first_name', 'cuil_cuim', 'email', 'profile_picture_short_tag',)
    search_fields = ['cuil_cuim', 'first_name', 'last_name', 'email', ]
    ordering = ('-is_active', 'last_name', 'first_name', )
    fields = (('email', 'password',), ('last_name', 'first_name',),'cuil_cuim',('mobile', 'phone',),
              ('profile_picture_medium_tag', 'profile_picture',), ('user_type', 'type',),('is_active','is_staff',),
              'description')
    minimum_fields = (('email',), ('last_name', 'first_name',),'cuil_cuim',('mobile', 'phone',),
              ('profile_picture_medium_tag', 'profile_picture',),'description')
    extra_fields = ('username', ('email', 'password',), ('last_name', 'first_name',),'cuil_cuim',('mobile', 'phone',),
            ('profile_picture_medium_tag', 'profile_picture',), ('user_type', 'type',),
            ('is_active', 'is_staff', 'is_superuser',),'description')

    readonly_fields = ('profile_picture_medium_tag', )
    list_filter = ('is_active', 'user_type', )

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        user = request.user

        if not user.is_superuser:
            if user.user_type == User.RECEPTIONIST:
                return qs.filter(Q(user_type=User.CITIZEN))

            elif user.user_type == User.ADMINISTRATOR:
                return qs.exclude(is_superuser=True)
            else:
                return qs.filter(pk=user.pk)

        return qs

    def get_list_filter(self, request):
        user = request.user
        user_type = user.user_type

        if user.is_superuser or user_type == User.RECEPTIONIST or user_type == User.ADMINISTRATOR:
            return super(UserAdmin, self).get_list_filter(request)
        else:
            return ()

    def get_list_display(self, request):
        user = request.user
        user_type = user.user_type

        if user.is_superuser or user_type == User.RECEPTIONIST or user_type == User.ADMINISTRATOR:
            return super(UserAdmin, self).get_list_display(request)
        else:
            return self.list_display_minimum

    def get_fields(self, request, obj=None):
        user = request.user
        if not user.is_superuser:
            user_type = user.user_type
            if user_type == User.RECEPTIONIST or user_type == User.SUPERVISOR:
                return self.minimum_fields

            elif user_type == User.ADMINISTRATOR:
                return self.fields
            else:
                return self.fields
        else:
            return self.extra_fields

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        user = request.user

        if db_field.name == 'status' and not user.is_superuser:
            if user.user_type == User.RECEPTIONIST:
                kwargs["choices"] = User.USER_TYPE_CHOICES_RECEPTIONIST

            elif user.user_type == User.ADMINISTRATOR:
                kwargs["choices"] = User.USER_TYPE_CHOICES_ADMINISTRATOR

            elif user.user_type == User.SUPERVISOR:
                kwargs["choices"] = User.USER_TYPE_CHOICES_SUPERVISOR

        return db_field.formfield(**kwargs)

    def save_model(self, request, obj, form, change):
        # obj.is_staff = obj.user_type != Person.SUBSCRIBER

        if 'email' in form.changed_data:
            obj.username = obj.email

        if 'password' in form.changed_data:
            obj.set_password(obj.password)
        obj.save()

        if 'user_type' in form.changed_data:
            obj.groups.clear()
            obj.save()
            admin_group_user = Group.objects.get(name=obj.user_type)
            admin_group_user.user_set.add(obj.pk)
            admin_group_user.save()


admin.site.register(User, UserAdmin)
