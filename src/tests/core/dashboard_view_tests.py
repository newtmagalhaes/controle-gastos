from http import HTTPStatus
from typing import Iterable

from django.db.models import QuerySet
from django.template.response import TemplateResponse
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from pytest import fixture

from .seeds import create_categoria


@fixture(scope='module')
def dashboard() -> str:
    return reverse('dashboard')


@fixture
def categoria(admin_user):
    despesa = create_categoria(admin_user)
    yield despesa
    despesa.delete()


def test_get_dashboard_today(dashboard, categoria, admin_client: Client):
    now = timezone.now().date()
    response = admin_client.get(dashboard)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)

    assert (object_list := response.context.get('object_list'))
    assert isinstance(object_list, (QuerySet, list,))

    assert len(itens := object_list[0].itens_despesas.all()) == 1
    assert itens[0].date.year == now.year
    assert itens[0].date.month == now.month


def test_get_empty_dashboard_today(dashboard, admin_client: Client):
    now = timezone.now().date()
    response = admin_client.get(dashboard)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)

    object_list = response.context.get('object_list')
    assert isinstance(object_list, (QuerySet, list,))
    assert len(object_list) == 0
