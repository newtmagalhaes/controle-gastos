from django.template import Context, Template
from pytest import mark
import pytest
from apps.django_chartjs import chartjs, utils


@mark.parametrize(
    argnames='raw',
    argvalues=(
        {'y': 5},
        {'y': 5, 'x': 2},
        {'y': 5, 'x': 2, 'label': 'label'},
        {'y': 5, 'label': 'label'},
    ))
def test_render_pie_data_point(raw: dict):
    c = chartjs.ChartjsPie('test_id', [raw])

    template = Template('datasets: {{ dp | safe }},')
    rendered = template.render(Context({'dp': c.datasets()}))

    expect_label = utils._get_label_from_dict(raw)
    result = {'labels': [expect_label], 'data': [raw['y']]}

    assert rendered == f"datasets: [{result}],"


def test_create_empty_pie_error():
    with pytest.raises(AssertionError):
        chartjs.ChartjsPie('test_id')


@mark.parametrize(argnames='range_size', argvalues=(1, 2, 3, 5, 10))
def test_render_data_series(range_size: int):
    data = [{'y': i} for i in range(range_size)]
    ds = chartjs.ChartjsLine('test_id', data)
    t = Template('dataseries: {{ ds | safe }},')
    rendered = t.render(Context({'ds': ds.datasets()}, autoescape=True))
    expected = (
        'dataseries: ['
        + ', '.join(map(str, data))
        + '],'
    )
    assert rendered == expected
