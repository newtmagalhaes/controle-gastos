from typing import Type

from django.template import Context, Template
from pytest import fixture

from .. import chartjs

_CHART_TYPES: list[Type[chartjs.ChartType]] = [
    chartjs.ChartjsPie,
    chartjs.ChartjsLine,
]


@fixture
def raw_data():
    return [
        {'y': 5, 'label': 'a'},
        {'y': 3, 'label': 'b'},
        {'y': 2, 'label': 'c'},
    ]


@fixture(params=_CHART_TYPES)
def any_chart(raw_data, request) -> chartjs.ChartType:
    return request.param('chart_test_id', raw_data)


def test_render_chart(any_chart):
    template = Template('{% load django_chartjs %}\n{% chart test_chart %}')
    context = Context({'test_chart': any_chart})
    template.render(context)
