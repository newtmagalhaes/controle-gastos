from typing import Any

from django import forms
from django.contrib import messages
from django.db import models
from django.db.models import Sum
from django.db.models.functions import Cast
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from apps.django_chartjs import chartjs

from ..forms import categoria_forms
from ..models import CategoriaDespesa

__all__ = (
    'CategoriasListView',
    'CategoriaDetailView',
    'CategoriasUpdateView',
)


class CategoriasListView(ListView):
    allow_empty = True
    template_name = 'core/categorias/list.html'

    def get_queryset(self):
        return (
            self.request.user.despesas
            .annotate(total=Sum('itens_despesas__value', default=0))
            .all()
        )


def _create_line_chart(despesa: CategoriaDespesa, id: str = 'dashboard_line_id'):
    line_data = [{
        'label': despesa.title,
        'data': list(despesa.itens_despesas.values(
            x=Cast('date', models.CharField()),
            y=Cast('value', models.FloatField()),
        )),
    }]
    return chartjs.ChartjsLine(id, line_data)


class CategoriaDetailView(DetailView):
    template_name = 'core/categorias/detail.html'

    def get_queryset(self):
        return self.request.user.despesas.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        categoria: CategoriaDespesa = self.get_object()
        context['line_chart'] = _create_line_chart(categoria)
        return context


class CategoriasUpdateView(UpdateView):
    template_name = 'core/categorias/form.html'
    form_class = categoria_forms.UpdateCategoriaDespesaForm
    formset_class = categoria_forms.ItemDespesaBulkUpdateFormset

    def get_queryset(self):
        return self.request.user.despesas.all()

    def get_success_url(self) -> str:
        return reverse('categorias_list')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # Chamada do pai já inclui form
        if 'formset' not in context:
            context['formset'] = self._get_formset()
        return context

    def _get_formset(self):
        formset_class = self.formset_class
        return formset_class(**self.get_form_kwargs())

    def _form_valid(self, form: forms.BaseModelForm, formset: forms.BaseModelFormSet) -> HttpResponse:
        if form.has_changed():
            self.object = form.save()
            messages.info(self.request, f'Categoria "{self.object.title}" alterada')

        if formset.has_changed():
            deleted_items = len(formset.deleted_forms)
            total_items = len(formset.save())
            created_items = len(formset.new_objects)
            msg = f"{created_items} criados. {total_items - created_items} alterados. {deleted_items} apagados."
            messages.info(self.request, msg)

        return HttpResponseRedirect(self.get_success_url())

    def _formset_invalid(self, formset):
        return self.render_to_response(self.get_context_data(formset=formset))

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()

        form = self.get_form()
        formset = self._get_formset()
        if form.is_valid():
            if formset.is_valid():
                return self._form_valid(form, formset)
            return self._formset_invalid(formset)
        return self.form_invalid(form)
