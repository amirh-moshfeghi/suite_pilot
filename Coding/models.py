from django.db import models


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
    material_group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    child_group = models.CharField(max_length=256, null=True)
    child_position = models.IntegerField(default=0)
    child_parent_id = models.IntegerField(default=0)
    child_value_id = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Child_Group'
        verbose_name_plural = 'Child_Groups'

    def __str__(self):
        return self.child_group


class Values(models.Model):
    material_group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    child_group = models.ForeignKey(Child, on_delete=models.CASCADE, null=True, related_name='child_group_related')
    value_abb = models.CharField(max_length=256, null=True)
    value_desc = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.value_desc


