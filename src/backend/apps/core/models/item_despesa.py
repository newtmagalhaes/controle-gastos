from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class ItemDespesa(models.Model):
    descricao = models.CharField(
        verbose_name='descrição', name='description', max_length=255,
        null=False, blank=True,
    )
    valor = models.DecimalField(
        verbose_name='valor', name='value', max_digits=10, decimal_places=2, null=False,
        blank=False, validators=[MinValueValidator(0)]
    )
    dia = models.DateField(
        verbose_name='dia', name='date', null=False, blank=False,
        help_text='dia que a despesa foi gerada'
    )
    hora = models.TimeField(
        verbose_name='hora', name='time', null=True, blank=True,
        help_text='hora que a despesa foi gerada (opcional)'
    )

    created_at = models.DateTimeField(
        verbose_name='criado em', name='created_at',
        auto_now_add=True, null=False, blank=False,
    )

    categoria = models.ForeignKey(
        to='CategoriaDespesa', on_delete=models.CASCADE,
        related_name='itens_despesas', null=False, blank=False
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='itens_despesas', null=False, blank=False,
    )

    class Meta:
        verbose_name = 'item de despesa'
        verbose_name_plural = 'itens de despesa'
