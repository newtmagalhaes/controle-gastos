from django.db.models import TextChoices


class ChartThemeChoices(TextChoices):
    LIGHT = 'light2', 'Claro'
    DARK = 'dark2', 'Escuro'


class ChartTypeChoices(TextChoices):
    PIE = 'pie', 'Pizza'
    BAR = 'bar', 'Barras'
    LINE = 'line', 'Linha'
