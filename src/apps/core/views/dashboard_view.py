from datetime import date

from django.db import models
from django.db.models.functions import Cast, TruncMonth
from django.db.models.manager import Manager
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


class PeriodFromParamsMixin:
    period_field = 'periodo'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)  # type: ignore
        context["period_field"] = self.get_period_field()
        return context

    def get_period_field(self) -> str:
        return self.period_field

    def get_date(self) -> date | None:
        '''return date if period is in params'''
        value = self.request.GET.get(self.get_period_field())  # type: ignore
        try:
            assert isinstance(value, str)
            year, month = map(int, value.split('-', maxsplit=1))
            return date(year, month, 1)

        except Exception:
            return


class DashboardView(PeriodFromParamsMixin, ListView):
    '''Exibe `CategoriaDespesa`s e `ItensDespesa`s do usuário
    do `ano-mês` atual ou especificado
    '''
    template_name = 'core/dashboard.html'

    def get_date(self) -> date:
        return super().get_date() or timezone.now().date().replace(day=1)

    def get_available_dates(self) -> list[str]:
        return list(
            self.request.user.itens_despesas
            .values(month=TruncMonth('date'))
            .annotate(count=models.Count('month'))
        )

    def get_queryset(self):
        selected_date = self.get_date()
        return categoria_despesas.list_non_empty_categorias_from_date(
            self.request.user.despesas,
            selected_date.month,
            selected_date.year,
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
