from django.db.models import Sum
from django.views.generic import ListView

from ..models import CategoriaDespesa


class CategoriasListView(ListView):
    model = CategoriaDespesa
    allow_empty = True
    template_name = 'core/archive/categorias_list.html'

    def get_queryset(self):
        assert self.model is not None
        return (
            self.request.user.despesas
            .annotate(total=Sum('itens_despesas__value', default=0))
            .all()
        )
