from django import forms

from ..models import CategoriaDespesa, ItemDespesa


class UpdateCategoriaDespesaForm(forms.ModelForm):
    class Meta:
        model = CategoriaDespesa
        fields = ['title', 'description']


class ItemDespesaModelForm(forms.ModelForm):
    class Meta:
        model = ItemDespesa
        fields = ['value', 'description', 'date', 'time']

    def save(self, commit: bool = True):
        '''Set instance user before save'''
        self.instance.user = self.instance.categoria.user
        return super().save(commit)


ItemDespesaBulkUpdateFormset = forms.inlineformset_factory(
    CategoriaDespesa,
    ItemDespesa,
    form=ItemDespesaModelForm,
    # edit_only=True,
    extra=1
)
