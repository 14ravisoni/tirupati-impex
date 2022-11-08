from django.db import models


class CodeParameter(models.Model):
    parameter_name = models.CharField(unique=True, max_length=100, blank=False, null=False)
    parameter_value = models.CharField(max_length=100, blank=False, null=False)
    parameter_active = models.BooleanField(blank=False, null=False, default=False)
    parameter_description = models.TextField(max_length=400, blank=False, null=False, default='')

    def __str__(self):
        return self.parameter_name
