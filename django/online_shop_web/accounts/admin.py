from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models
from . import forms


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', )
    readonly_fields = ('id', 'date_joined', 'last_login')
    exclude = ('username', 'password', )
    ordering = ['email', ]

    add_form = forms.CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(models.CustomUser, CustomUserAdmin)
