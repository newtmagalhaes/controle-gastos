from typing import Any

from django import template

register = template.Library()


@register.filter
def to_brl(value: float) -> str:
    coerced = float(value)
    return f'R$ {coerced:.2f}'


@register.inclusion_tag('core/widgets/accordion.html')
def accordion(widgets: list[tuple[str, Any]], parent_id='accordion'):
    return {
        'parent_id': parent_id,
        'items': [
            (f'{parent_id}-{i}', name, value)
            for i, (name, value) in enumerate(widgets)
        ],
    }
