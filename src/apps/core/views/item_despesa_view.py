from django.contrib import messages
from django.urls import reverse
from django.views.generic import DeleteView


class ItemDespesaDeleteView(DeleteView):
    def get_queryset(self):
        return self.request.user.itens_despesas

    def get_success_url(self) -> str:
        item = self.get_object()
        messages.info(self.request, f'Item ({item}) excluido.')
        url = reverse('item_despesa_update', kwargs={'pk': item.categoria_id})
        return url
