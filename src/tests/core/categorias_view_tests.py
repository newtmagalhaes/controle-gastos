from http import HTTPStatus

from django.forms import Form
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from pytest import fixture

from apps.core import models
from apps.manager.models import CustomUser


@fixture(scope='module')
def endpoint() -> str:
    return reverse('categorias_list')


def _categoria_update(pk):
    return reverse('categoria_update', kwargs={'pk': pk})


@fixture
def multiple_users(db):
    '''Create multiple users and one related `CategoriaDespesa` for each'''
    users = CustomUser.objects.bulk_create(
        CustomUser(username=f'user {i}')
        for i in range(3)
    )
    yield users
    # Delete users and categories after test
    CustomUser.objects.filter(username__in=(u.username for u in users)).delete()


@fixture
def current_user(multiple_users):
    return multiple_users[0]


@fixture
def logged_client(client: Client, current_user):
    client.force_login(current_user)
    yield client
    client.logout()


@fixture
def multiple_categorias(multiple_users: list[CustomUser]):
    models.CategoriaDespesa.objects.bulk_create(
        models.CategoriaDespesa(title=f'cat {i}', description=f'desc {i}', user=user)
        for i, user in enumerate(multiple_users)
    )


def test_listar_categorias(admin_client: Client, db, endpoint):
    response = admin_client.get(endpoint, follow=True)

    assert response.status_code == HTTPStatus.OK


def test_list_own_categories(client: Client, multiple_users, multiple_categorias, endpoint):
    client.force_login(multiple_users[0])

    response = client.get(endpoint)

    assert response.status_code == HTTPStatus.OK
    assert (categorias := response.context.get('object_list')) is not None
    assert len(categorias) == 1


def test_show_categoria_update(logged_client: Client, current_user, multiple_categorias):
    categoria = current_user.despesas.first()
    assert isinstance(categoria, models.CategoriaDespesa)

    response = logged_client.get(_categoria_update(categoria.id))

    assert response.status_code == HTTPStatus.OK


def test_save_categoria_update(logged_client: Client, current_user, multiple_categorias, endpoint):
    categoria = current_user.despesas.first()
    assert isinstance(categoria, models.CategoriaDespesa)

    initial = logged_client.get(_categoria_update(categoria.id))
    assert isinstance(initial, TemplateResponse)
    assert initial.status_code == HTTPStatus.OK

    body = _to_body(initial.context['form'])
    body['title'] = 'changed title'

    initial_formset = initial.context['formset']
    body.update(_to_body(initial_formset.management_form))
    body.update(*[_to_body(form) for form in initial_formset])
    body[f'{initial_formset.prefix}-0-value'] = 42
    body[f'{initial_formset.prefix}-0-date'] = timezone.now().date()

    response = logged_client.post(_categoria_update(categoria.id), data=body)

    assert isinstance(response, HttpResponseRedirect)
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == endpoint


def test_save_categoria_update_fail_form(logged_client: Client, current_user, multiple_categorias, endpoint):
    categoria = current_user.despesas.first()
    assert isinstance(categoria, models.CategoriaDespesa)

    initial = logged_client.get(_categoria_update(categoria.id))
    assert isinstance(initial, TemplateResponse)
    assert initial.status_code == HTTPStatus.OK

    body = _to_body(initial.context['form'])
    # title can't be empty
    body['title'] = ''

    initial_formset = initial.context['formset']
    body.update(_to_body(initial_formset.management_form))
    body.update(*[_to_body(form) for form in initial_formset])

    response = logged_client.post(_categoria_update(categoria.id), data=body)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)

    form = response.context['form']
    assert form.is_valid() is False
    assert 'title' in form.errors
    assert response.context['formset'].is_valid() is True


def test_save_categoria_update_fail_formset(logged_client: Client, current_user, multiple_categorias, endpoint):
    categoria = current_user.despesas.first()
    assert isinstance(categoria, models.CategoriaDespesa)

    initial = logged_client.get(_categoria_update(categoria.id))
    assert initial.status_code == HTTPStatus.OK
    assert isinstance(initial, TemplateResponse)

    body = _to_body(initial.context['form'])

    initial_formset = initial.context['formset']
    body.update(_to_body(initial_formset.management_form))
    body.update(*[_to_body(form) for form in initial_formset])
    # date is a required field
    body[f'{initial_formset.prefix}-0-value'] = 42

    response = logged_client.post(_categoria_update(categoria.id), data=body)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)

    formset = response.context['formset']
    assert response.context['form'].is_valid()
    assert response.context['formset'].is_valid() is False
    assert any('date' in errors for errors in formset.errors)


def _to_body(form: Form):
    return {
        field.id_for_label.removeprefix('id_'): field.value()
        for field in form
        if field.value() is not None
    }
