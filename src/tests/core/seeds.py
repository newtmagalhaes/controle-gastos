from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from apps.core import models


def create_categoria(user: AbstractUser):
    '''Cria categoria com 1 item por mês ao longo do ano'''
    despesa = models.CategoriaDespesa.objects.create(
        title='categoria',
        description='descrição',
        user=user,
    )
    now = timezone.now().date()
    models.ItemDespesa.objects.bulk_create(
        models.ItemDespesa(
            value=10 * i,
            date=now.replace(month=i, day=i),
            user=user,
            categoria=despesa,
        )
        for i in range(1, 13)
    )
    return despesa
