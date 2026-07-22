import uuid

from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.models import AutoField, UUIDField

BaseDatabaseOperations.integer_field_ranges['UUIDField'] = (0, 0)


class UUIDAutoField(UUIDField, AutoField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', uuid.uuid4)
        # kwargs.setdefault('max_length', 32)
        kwargs.setdefault('editable', False)
        super().__init__(*args, **kwargs)

    def _check_max_length_warning(self):
        '''Disable max_length warning'''
        return []

    def get_prep_value(self, value):
        return self.to_python(value)
