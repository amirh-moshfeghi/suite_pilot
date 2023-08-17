from django.db import models
from django_jsonform.models.fields import JSONField


class MaterialGroup(models.Model):
    material_group = models.CharField(max_length=250)
    material_parent_id = models.IntegerField(default=0)
    identity_reference = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                           )
    material_abb = models.CharField(max_length=250, null=True)
    is_parent = models.BooleanField(default=False)
    parent_child_id = models.IntegerField(default=0)

    # @property
    # def identity_reference_name_assign(self):
    #        return self.identity_reference.material_group

    class Meta:
        verbose_name = 'Material_Group'
        verbose_name_plural = 'Material_Groups'

    def __str__(self):
        return self.material_group


class Child(models.Model):
    ITEMS_SCHEMA = {
    'type': 'list',
    'items': {
        'type': 'dict',
        'keys': {
            'description': {
                'type': 'string'
            },
            'abbr': {
                'type': 'string'
            },

        }
    }
}

    material_group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    child_group = models.CharField(max_length=256, null=True)
    child_position = models.IntegerField(default=0)
    child_parent_id = models.IntegerField(default=0)
    child_desc = JSONField(schema=ITEMS_SCHEMA, null=True)


    class Meta:
        verbose_name = 'Child_Group'
        verbose_name_plural = 'Child_Groups'

    def __str__(self):
        return self.child_group




