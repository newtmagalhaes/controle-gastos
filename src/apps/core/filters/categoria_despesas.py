from django.db import models

from ..models import CategoriaDespesa, ItemDespesa


def list_non_empty_categorias_from_date(
        qs: models.Manager[CategoriaDespesa],
        month: int,
        year: int,
        ) -> models.Manager[CategoriaDespesa]:
    '''List `CategoriaDespesa` with `ItemDespesa` from month/year'''
    users = set(qs.values_list('user_id', flat=True))
    related_itens = ItemDespesa.objects.filter(user_id__in=users, date__month=month, date__year=year)
    itens_despesas_sum_field = models.Sum(
        'itens_despesas__value',
        default=0,
        filter=models.Q(itens_despesas__date__month=month, itens_despesas__date__year=year)
    )
    return (
        qs.prefetch_related(models.Prefetch('itens_despesas', related_itens))
        .annotate(itens_despesas_sum=itens_despesas_sum_field)
        .filter(itens_despesas_sum__gt=0)
    )
