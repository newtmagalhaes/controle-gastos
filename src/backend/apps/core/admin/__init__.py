from django.contrib import admin

from ...core import models

# Register your models here.


@admin.register(models.CategoriaDespesa)
class CategoriaDespesaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ItemDespesa)
class ItemDespesaAdmin(admin.ModelAdmin):
    pass
