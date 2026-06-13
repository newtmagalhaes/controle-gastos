from django.conf import settings
from django.views.generic import MonthArchiveView

from ..models import ItemDespesa


class DespesasMensaisView(MonthArchiveView):
    model = ItemDespesa
    ordering = ['-date']
    date_field = 'date'
    month_format = '%m'
    allow_empty = True
    paginate_by = settings.DEFAULT_PAGE_SIZE
    template_name = 'core/archive/despesas_mensais.html'

    def get_queryset(self):
        assert self.model is not None
        ordering = self.get_ordering() or []
        return (
            self.model.objects
            .filter(user=self.request.user)
            .select_related('categoria')
            .order_by(*ordering)
            .all()
        )
