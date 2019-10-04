from django.contrib import admin
from .models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Currency, CurrencyAdmin)