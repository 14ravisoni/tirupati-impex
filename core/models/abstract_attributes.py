from django.db import models


class DateTimeAbstract(models.Model):
    created_date_time = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_date_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class DescriptionRemarkAbstract(models.Model):
    description = models.TextField(max_length=400, null=True, default='')
    remarks = models.TextField(max_length=400, null=True, default='')

    class Meta:
        abstract = True
