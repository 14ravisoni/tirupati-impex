from django.db import models

from .abstract_attributes import DescriptionRemarkAbstract, DateTimeAbstract
from ..models import Worker


class JewlType(DescriptionRemarkAbstract):
    type_name = models.CharField(unique=True, max_length=100, null=False)
    type_code = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.type_name


class JewlStage(DescriptionRemarkAbstract):
    stage = models.CharField(unique=True, max_length=100, null=True)

    def __str__(self):
        return self.stage


class Jewl(DateTimeAbstract, DescriptionRemarkAbstract):
    jewl_id = models.CharField(unique=True, max_length=10, null=True)
    jewl_type = models.ForeignKey(JewlType, on_delete=models.CASCADE)
    stage = models.ForeignKey(JewlStage, on_delete=models.CASCADE)
    issue_weight = models.DecimalField(max_digits=10, null=True, decimal_places=3)
    net_weight = models.DecimalField(max_digits=10, null=True, decimal_places=3)
    kundan_weight = models.DecimalField(max_digits=10, null=True, decimal_places=3)
    gross_weight = models.DecimalField(max_digits=10, null=True, decimal_places=3)

    class Meta:
        ordering = ['jewl_id']

    def __str__(self):
        return self.jewl_id


class JewlImage(DateTimeAbstract):
    jewl_id = models.ForeignKey(Jewl, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=300, null=True)
    stage = models.ForeignKey(JewlStage, on_delete=models.CASCADE)


class JewlStageTransaction(DateTimeAbstract, DescriptionRemarkAbstract):
    jewl = models.ForeignKey(Jewl, on_delete=models.CASCADE)
    stage = models.ForeignKey(JewlStage, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    expected_finish_date_time = models.DateTimeField(null=True, blank=True)
