from datetime import datetime

from django.contrib import admin
from django.utils import timezone

from ...core import models

# Register your models here.


@admin.register(models.CategoriaDespesa)
class CategoriaDespesaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_owner', 'id',)
    list_display_links = ('title', 'id',)
    list_select_related = ('user',)

    @admin.display(description='dono')
    def category_owner(self, obj: models.CategoriaDespesa):
        return obj.user.username


@admin.register(models.ItemDespesa)
class ItemDespesaAdmin(admin.ModelAdmin):
    list_display = ('category_owner', 'value', 'date_time', 'id',)
    list_display_links = ('value', 'id')
    list_select_related = ('user',)

    @admin.display(description='dono')
    def category_owner(self, obj: models.CategoriaDespesa):
        return obj.user.username

    @admin.display(description='dia e hora')
    def date_time(self, obj: models.ItemDespesa):
        return obj.date if obj.time is None else datetime.combine(obj.date, obj.time, timezone.get_current_timezone())
