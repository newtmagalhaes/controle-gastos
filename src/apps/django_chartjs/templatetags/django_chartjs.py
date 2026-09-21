from django import template

register = template.Library()


@register.inclusion_tag('django_chartjs/base_chart.html')
def chart(custom_chart):
    return {'chart': custom_chart}


@register.inclusion_tag('django_chartjs/head.html')
def chart_js():
    return {}
