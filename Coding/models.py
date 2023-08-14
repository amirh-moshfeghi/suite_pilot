from django.db import models

class MaterialGroup(models.Model):
    material_group = models.CharField(max_length=250)
    parent_id = models.IntegerField(default=0)
    abb = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = 'Material_Group'
        verbose_name_plural = 'Material_Groups'

    def __str__(self):
        return self.material_group


class IdentityGroup(models.Model):
    material_group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    identity_group = models.CharField(max_length=256, null=True)
    # parent_id = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    abb = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = 'Identity_Group'
        verbose_name_plural = 'Identity_Groups'

    def __str__(self):
        return self.identity_group


class Child(models.Model):
    material_group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    # description = models.TextField(default="")
    identity_group = models.ForeignKey(IdentityGroup, on_delete=models.CASCADE)
    # parent_id = models.ForeignKey(IdentityGroup, on_delete=models.CASCADE)
    child_group = models.CharField(max_length=250, null=True)
    position = models.CharField(max_length=256, null=True)
    child_id_as_parent = models.CharField(max_length=256,null=True)




    class Meta:
        verbose_name = 'Child_Group'
        verbose_name_plural = 'Child_Groups'

    def __str__(self):
        return self.child_group


class Values(models.Model):
    material_group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    # description = models.TextField(default="")
    identity_group = models.ForeignKey(IdentityGroup, on_delete=models.CASCADE)
    # parent_id = models.ForeignKey(IdentityGroup, on_delete=models.CASCADE)
    child_group = models.ForeignKey(Child, on_delete=models.CASCADE, null=True, related_name='child_group_related')
    child_abb = models.CharField(max_length=256, null=True)
    child_desc = models.CharField(max_length=256, null=True)
    value = models.CharField(max_length=256, null=True)
    # child_id_as_child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True, related_name='child_child_id_related')
    child_id_as_value = models.CharField(max_length=256,null=True)


    def __str__(self):
        return self.value


class SP(models.Model):
    material_group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    # description = models.TextField(default="")
    identity_group = models.ForeignKey(IdentityGroup, on_delete=models.CASCADE)
    # parent_id = models.ForeignKey(IdentityGroup, on_delete=models.CASCADE)
    child_group = models.ForeignKey(Child, on_delete=models.CASCADE, null=True)
    value = models.ForeignKey(Values, on_delete=models.CASCADE, null=True)
    sp = models.CharField(max_length=256,null=True)

    def __str__(self):
        return self.sp

