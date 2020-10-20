from django.contrib import admin

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'name',)
    list_filter = ('email', 'name',  'is_active', 'is_staff')
    ordering = ('-created_at',)
    list_display = ('email', 'name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'first_name',
                           'last_name', 'phone', 'session_token', 'gender', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name',  'password', 'first_name',
                       'last_name', 'phone',  'gender', 'is_active', 'session_token', 'last_login',  'is_staff')}
         ),
    )


admin.site.register(CustomUser)
