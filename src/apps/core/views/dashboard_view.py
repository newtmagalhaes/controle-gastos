from datetime import date

from django.db import models
from django.db.models.manager import Manager
from django.db.models.functions import Cast, TruncMonth
from django.utils import timezone
from django.views.generic import ListView

from apps.django_chartjs import chartjs

from ..filters import categoria_despesas
from ..models import CategoriaDespesa


def _create_line_chart(qs: Manager[CategoriaDespesa], id: str = 'dashboard_line_id'):
    line_data = [
        {
            'label': despesa.title,
            'data': list(despesa.itens_despesas.values(
                x=Cast('date', models.CharField()),
                y=Cast('value', models.FloatField()),
            )),
        }
        for despesa in qs
    ]
    return chartjs.ChartjsLine(id, line_data)


def _create_pie_chart(qs: Manager[CategoriaDespesa], id: str = 'dashboard_pie_id'):
    pie_data = list(qs.values(label=models.F('title'), y=Cast('itens_despesas_sum', models.FloatField())))
    return chartjs.ChartjsPie(id, pie_data)


class DashboardView(ListView):
    template_name = 'core/dashboard.html'

    def get_date(self) -> date:
        return timezone.now().date()

    def get_available_dates(self) -> list[str]:
        return list(
            self.request.user.itens_despesas
            .values(month=TruncMonth('date'))
            .annotate(count=models.Count('month'))
        )

    def get_queryset(self):
        d = self.get_date()
        return categoria_despesas.list_non_empty_categorias_from_date(
            self.request.user.despesas,
            d.month,
            d.year,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        if len(queryset) > 0:
            context.setdefault('pie_chart', _create_pie_chart(queryset))
            context.setdefault('line_chart', _create_line_chart(queryset))

        context.setdefault('selected_date', self.get_date())
        context.setdefault('available_dates', self.get_available_dates())
        return context
