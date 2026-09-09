from typing import Any

from django import forms
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect


class ExtraFormsetMixin:
    formset_class = None

    def get_formset_class(self) -> forms.BaseModelFormSet:
        return self.formset_class

    def get_formset(self):
        formset_class = self.get_formset_class()
        return formset_class(**self.get_form_kwargs())

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # Chamada do pai já inclui form
        if 'formset' not in context:
            context['formset'] = self.get_formset()
        return context


class ProcessExtraFormsetMixin:
    def both_forms_valid(self, form: forms.BaseModelForm, formset: forms.BaseModelFormSet) -> HttpResponse:
        if form.has_changed():
            self.object = form.save()
            messages.info(self.request, f'Categoria "{self.object.title}" alterada')

        if formset.has_changed():
            deleted_items = len(formset.deleted_forms)
            total_items = len(formset.save())
            created_items = len(formset.new_objects)
            msg = f"{created_items} criados. {total_items - created_items} alterados. {deleted_items} apagados."
            messages.info(self.request, msg)

        return HttpResponseRedirect(self.get_success_url())

    def formset_invalid(self, formset) -> HttpResponse:
        return self.render_to_response(self.get_context_data(formset=formset))
