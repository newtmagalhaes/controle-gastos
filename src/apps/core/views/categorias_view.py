from typing import Any

from django.contrib import messages
from django.db import models
from django.db.models import Sum
from django.db.models.functions import Cast
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from apps.django_chartjs import chartjs


from ..forms import categoria_forms
from ..models import CategoriaDespesa

__all__ = (
    'CategoriasListView',
    'CategoriaDetailView',
    'CategoriasUpdateView',
    'CategoriaBulkUpdateView',
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
    slug_field = 'id'

    def get_queryset(self):
        return self.request.user.despesas

    def get_success_url(self) -> str:
        return reverse('categorias_list')


class CategoriaBulkUpdateView(UpdateView):
    template_name = 'core/categorias/formset.html'

    form_class = categoria_forms.ItemDespesaBulkUpdateFormset  # type: ignore

    def get_queryset(self):
        return self.request.user.despesas.all()

    def get_success_url(self) -> str:
        categoria = self.get_object()
        messages.success(self.request, f'Categoria {categoria.title}')
        return reverse('categorias_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
