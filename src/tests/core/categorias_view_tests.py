from http import HTTPStatus

from django.test import Client
from django.urls import reverse
from pytest import mark, fixture


@fixture(scope='module')
def endpoint() -> str:
    return reverse('categorias_list')


def test_listar_categorias(admin_client: Client, db, endpoint):
    response = admin_client.get(endpoint, follow=True)

    assert response.status_code == HTTPStatus.OK
