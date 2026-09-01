from datetime import date
from http import HTTPStatus

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
    current_month = timezone.now().date()
    response = admin_client.get(dashboard)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)

    selected_date = response.context.get('selected_date')
    assert isinstance(selected_date, date)
    assert selected_date.month == current_month.month
    assert selected_date.year == current_month.year

    assert (object_list := response.context.get('object_list'))
    assert isinstance(object_list, (QuerySet, list,))

    assert len(itens := object_list[0].itens_despesas.all()) == 1
    assert itens[0].date.year == current_month.year
    assert itens[0].date.month == current_month.month


def _get_random_month(today: date) -> date:
    from random import randint
    value = today.month
    while value == today.month:
        value = randint(1, 12)
    return today.replace(month=value)


def test_get_dashboard_from_specific_month(dashboard, categoria, admin_client: Client):
    random_month = _get_random_month(timezone.now().date().replace(day=1))
    response = admin_client.get(dashboard, query_params={'periodo': random_month.strftime('%Y-%m')})  # type: ignore

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)

    selected_date = response.context.get('selected_date')
    assert isinstance(selected_date, date)
    assert selected_date.month == random_month.month
    assert selected_date.year == random_month.year

    assert (object_list := response.context.get('object_list'))
    assert isinstance(object_list, (QuerySet, list,))

    assert len(itens := object_list[0].itens_despesas.all()) == 1
    assert itens[0].date.year == random_month.year
    assert itens[0].date.month == random_month.month


def test_get_empty_dashboard_today(dashboard, admin_client: Client):
    current_month = timezone.now().date()
    response = admin_client.get(dashboard)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)

    selected_date = response.context.get('selected_date')
    assert isinstance(selected_date, date)
    assert selected_date.month == current_month.month
    assert selected_date.year == current_month.year

    object_list = response.context.get('object_list')
    assert isinstance(object_list, (QuerySet, list,))
    assert len(object_list) == 0
