from django import template

register = template.Library()


@register.filter
def to_brl(value: float) -> str:
    coerced = float(value)
    return f'R$ {coerced:.2f}'
