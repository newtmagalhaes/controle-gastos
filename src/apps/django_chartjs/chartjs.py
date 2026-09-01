from dataclasses import dataclass
from numbers import Number
from typing import Any, Literal

from . import utils
from .constants import ChartThemeChoices, ChartTypeChoices

Dataset = dict[Literal['data'] | str, Any]


@dataclass
class ChartType:
    '''Base class for charts
    ------------------------
    @param id: must be unique for template
    '''
    id: str
    _datasets: list[Dataset]
    type: ChartTypeChoices
    theme: ChartThemeChoices = ChartThemeChoices.DARK

    def datasets(self) -> list[Dataset]:
        return self._datasets

    def labels(self) -> list[str]:
        return getattr(self, '_labels', [])

    def options(self) -> dict:
        return getattr(self, '_options', {})


class ChartjsPie(ChartType):

    def __init__(
            self,
            id: str,
            data: list[dict] = [],
            *,
            labels: list[str] = [],
            values: list[Number] = [],
            ) -> None:
        '''Pie chart
        ------------
        @param data: dicts containing labels and values;
        @param labels: strings for labels;
        @param values: numeric values.
        '''
        assert data or (labels and values), "'data' or 'labels' and 'values' cannot be empty"

        dataset = [{
            'data': values or list(map(utils._get_y_from_dict, data))
        }]
        super().__init__(id, dataset, ChartTypeChoices.PIE)
        self._labels = labels or list(map(utils._get_label_from_dict, data))


class ChartjsLine(ChartType):
    def __init__(self, id: str, data: list[Dataset]) -> None:
        super().__init__(id, data, ChartTypeChoices.LINE)
