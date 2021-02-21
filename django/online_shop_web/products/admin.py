from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', )
    readonly_fields = ('created_at', )


admin.site.register(models.Product, ProductAdmin)

