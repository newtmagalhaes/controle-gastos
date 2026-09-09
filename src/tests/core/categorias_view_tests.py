from http import HTTPStatus

from django.test import Client
from django.urls import reverse
from pytest import fixture

from apps.core import models
from apps.manager.models import CustomUser


@fixture(scope='module')
def endpoint() -> str:
    return reverse('categorias_list')


def _categoria_detail(pk):
    return reverse('categoria_detail', kwargs={'pk': pk})


def _categoria_update(pk):
    return reverse('categoria_update', kwargs={'pk': pk})


@fixture
def multiple_users(db):
    '''Create multiple users (yields first) and one related `CategoriaDespesa` for each'''
    users = CustomUser.objects.bulk_create(
        CustomUser(username=f'user {i}')
        for i in range(3)
    )
    yield users
    # Delete users and categories after test
    CustomUser.objects.filter(username__in=(u.username for u in users)).delete()


@fixture
def multiple_categorias(multiple_users: list[CustomUser]):
    models.CategoriaDespesa.objects.bulk_create(
        models.CategoriaDespesa(title=f'cat {i}', user=user)
        for i, user in enumerate(multiple_users)
    )
    # yield


def test_listar_categorias(admin_client: Client, db, endpoint):
    response = admin_client.get(endpoint, follow=True)

    assert response.status_code == HTTPStatus.OK


def test_list_own_categories(client: Client, multiple_users, multiple_categorias, endpoint):
    client.force_login(multiple_users[0])

    response = client.get(endpoint)

    assert response.status_code == HTTPStatus.OK
    assert (categorias := response.context.get('object_list')) is not None
    assert len(categorias) == 1


def test_show_categoria(client: Client, multiple_users, multiple_categorias):
    user = multiple_users[0]
    categoria = user.despesas.first()
    assert isinstance(categoria, models.CategoriaDespesa)

    client.force_login(user)
    response = client.get(_categoria_detail(categoria.id))

    assert response.status_code == HTTPStatus.OK


def test_show_categoria_update(client: Client, multiple_users, multiple_categorias):
    user = multiple_users[0]
    categoria = user.despesas.first()
    assert isinstance(categoria, models.CategoriaDespesa)

    client.force_login(user)
    response = client.get(_categoria_update(categoria.id))

    assert response.status_code == HTTPStatus.OK
