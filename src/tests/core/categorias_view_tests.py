from http import HTTPStatus

from django.test import Client
from django.urls import reverse
from pytest import fixture

from apps.core import models
from apps.manager.models import CustomUser


@fixture(scope='module')
def endpoint() -> str:
    return reverse('categorias_list')


@fixture
def multiple_users(db):
    '''Create multiple users (yields first) and one related `CategoriaDespesa` for each'''
    users = CustomUser.objects.bulk_create(
        CustomUser(username=f'user {i}')
        for i in range(3)
    )
    models.CategoriaDespesa.objects.bulk_create(
        models.CategoriaDespesa(title=f'cat {i}', user=user)
        for i, user in enumerate(users)
    )
    yield users[0]
    # Delete users and categories after test
    CustomUser.objects.filter(username__in=(u.username for u in users)).delete()


def test_listar_categorias(admin_client: Client, db, endpoint):
    response = admin_client.get(endpoint, follow=True)

    assert response.status_code == HTTPStatus.OK


def test_list_own_categories(client: Client, multiple_users, endpoint):
    client.force_login(multiple_users)

    response = client.get(endpoint)

    assert response.status_code == HTTPStatus.OK
    assert (categorias := response.context.get('object_list')) is not None
    assert len(categorias) == 1
