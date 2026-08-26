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
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'time': forms.widgets.TimeInput(attrs={'type': 'time'}),
        }

    def save(self, commit: bool = True):
        '''Set instance user before save'''
        self.instance.user = self.instance.categoria.user
        return super().save(commit)


ItemDespesaBulkUpdateFormset = forms.inlineformset_factory(
    CategoriaDespesa,
    ItemDespesa,
    form=ItemDespesaModelForm,
    extra=0,
)
