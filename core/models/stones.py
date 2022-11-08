from django.db import models

from core.models import Jewl


class Stone(models.Model):
    stone_name = models.CharField(unique=True, max_length=100, null=False)

    def __str__(self):
        return self.stone_name


class StoneJadaiTransaction(models.Model):
    jewl = models.ForeignKey(Jewl, on_delete=models.CASCADE)
    stone = models.ForeignKey(Stone, on_delete=models.CASCADE)
    karat = models.DecimalField(max_digits=10, null=True, decimal_places=3)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.jewl.jewl_id + ':' + self.stone.stone_name + ':' + self.quantity
