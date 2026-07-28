from typing import Any

from django.urls import reverse
from django.utils import timezone
from django.views.generic import RedirectView

# Register your views here
from .categorias_view import CategoriasListView
from .dashboard_view import DashboardView
from .despesas_mensais_view import DespesasMensaisView


class MesAtualRedirectView(RedirectView):
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        today = timezone.now()
        year = today.year
        month = today.month
        return reverse('despesas_mensais', kwargs={'year': year, 'month': month})
