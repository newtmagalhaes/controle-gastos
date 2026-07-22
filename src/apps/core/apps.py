from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'apps.manager.fields.UUIDAutoField'
    name = 'apps.core'
    verbose_name = 'Controle de Gastos'
