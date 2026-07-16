from django.conf import settings
from django.db.models import Sum
from django.views.generic import ListView

from ..models import CategoriaDespesa


class CategoriasListView(ListView):
    model = CategoriaDespesa
    ordering = ['titulo']
    allow_empty = True
    template_name = 'core/archive/categorias_list.html'

    def get_queryset(self):
        assert self.model is not None
        ordering = self.get_ordering() or []
        return (
            self.model.objects
            .filter(user=self.request.user)
            .annotate(total=Sum('itens_despesas__value', default=0))
            .order_by(*ordering)
            .all()
        )
