from django.db import models

class Material_Group(models.Model):
    name = models.CharField(max_length=30)
    Material_id = models.CharField(max_length=30)
    abbr = models.CharField(max_length=30)
    parent_id = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Identity_Group(models.Model):
    name = models.ForeignKey(Material_Group, on_delete=models.CASCADE, related_name='Identity_Group_name')
    Identity_id = models.ForeignKey(Material_Group, on_delete=models.CASCADE,related_name='Identity_Group_identity_id')
    abbr = models.ForeignKey(Material_Group, on_delete=models.CASCADE,related_name='Identity_Group_abbr')
    parent_id = models.ForeignKey(Material_Group, on_delete=models.CASCADE, related_name='Identity_Group_parent_id')

    def __str__(self):
        return self.name

class Child_Specs(models.Model):
    parent_name = models.ForeignKey(Identity_Group, on_delete=models.SET_NULL, null=True, related_name='Child_Specs_parent_name')
    parent_id = models.ForeignKey(Identity_Group, on_delete=models.SET_NULL, null=True,related_name='Child_Specs_parent_id')
    name = models.ForeignKey(Identity_Group, on_delete=models.SET_NULL, null=True, related_name='Child_Specs_name')
    value = models.ForeignKey(Identity_Group, on_delete=models.SET_NULL, null=True, related_name='Child_Specs_value')


    def __str__(self):
        return self.name