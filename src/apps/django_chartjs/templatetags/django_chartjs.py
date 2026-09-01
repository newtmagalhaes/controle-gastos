from django import template

from ..chartjs import ChartType

register = template.Library()


@register.inclusion_tag('django_chartjs/base_chart.html')
def chart(custom_chart: ChartType):
    assert isinstance(custom_chart, ChartType)
    return {'chart': custom_chart}


@register.inclusion_tag('django_chartjs/head.html')
def chart_js():
    return {}
