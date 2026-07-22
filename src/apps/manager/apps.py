from django.apps import AppConfig


class ManagementConfig(AppConfig):
    default_auto_field = 'apps.manager.fields.UUIDAutoField'
    name = 'apps.manager'
    verbose_name = 'Gerenciamento'
