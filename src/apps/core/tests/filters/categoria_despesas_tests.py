from django.utils import timezone
from pytest import fixture

from apps.core import models
from apps.core.filters import categoria_despesas


@fixture
def create_categorias(admin_user):
    '''Cria uma categoria vazia e outra com itens:
    um item para cada mês.
    '''
    empty_categoria = models.CategoriaDespesa.objects.create(
        title='empty',
        description='empty category',
        user=admin_user,
    )
    not_empty_categoria = models.CategoriaDespesa.objects.create(
        title='test',
        description='test category',
        user=admin_user,
    )
    current_date = timezone.now().date()
    models.ItemDespesa.objects.bulk_create([
        models.ItemDespesa(
            value=float(10 * i),
            date=current_date.replace(month=i, day=i),
            categoria=not_empty_categoria,
            user=admin_user,
        )
        for i in range(1, 13)
    ])
    yield

    not_empty_categoria.delete()
    empty_categoria.delete()


def test_return_non_empty_categorias(create_categorias, admin_user):
    '''Testa listagem de categorias somente com itens do mês atual'''
    now = timezone.now()
    result = categoria_despesas.list_non_empty_categorias_from_date(admin_user.despesas, now.month, now.year)

    assert len(result) == 1
    assert len(result[0].itens_despesas.all()) == 1
