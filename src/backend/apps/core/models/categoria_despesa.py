from django.conf import settings
from django.db import models


class CategoriaDespesa(models.Model):
    titulo = models.CharField(
        verbose_name='título', name='titulo', max_length=75,
        blank=False, null=False,
    )
    descricao = models.CharField(
        verbose_name='descrição', name='description', max_length=75,
        blank=False, null=False,
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='despesas', null=False, blank=False,
    )
    # itens_despesa: RelatedManager[ItemDespesa]

    class Meta:
        verbose_name = 'categoria de despesa'
        verbose_name_plural = 'categorias de despesas'
