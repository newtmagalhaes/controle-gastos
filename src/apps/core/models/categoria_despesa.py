from django.conf import settings
from django.db import models


class CategoriaDespesa(models.Model):
    title = models.CharField(
        verbose_name='título', max_length=75,
        blank=False, null=False,
    )
    description = models.CharField(
        verbose_name='descrição', max_length=75,
        blank=False, null=False,
    )

    created_at = models.DateTimeField(
        verbose_name='criado em', name='created_at',
        auto_now_add=True, null=False, blank=False,
        db_index=True,
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='despesas', null=False, blank=False,
    )
    # itens_despesas: RelatedManager[ItemDespesa]

    class Meta:
        verbose_name = 'categoria de despesa'
        verbose_name_plural = 'categorias de despesas'
        ordering = ['title']

    def __str__(self) -> str:
        return f'Categoria[{self.pk}]({self.title})'
