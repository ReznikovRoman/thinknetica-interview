from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', )
    search_fields = ('email', )
    readonly_fields = ('id', 'date_joined', 'last_login')
    exclude = ('username', 'password', )
    ordering = ['email', ]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(models.CustomUser, CustomUserAdmin)
