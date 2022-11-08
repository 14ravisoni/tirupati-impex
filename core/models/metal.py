from django.db import models

from .abstract_attributes import DescriptionRemarkAbstract, DateTimeAbstract


class Metal(DescriptionRemarkAbstract, DateTimeAbstract):
    quantity = models.DecimalField(max_digits=10, decimal_places=3, null=False, default=0.000)
    is_credit = models.BooleanField(blank=False, default=True, null=False)

    def __str__(self):
        return 'Quantity: ' + ('+' if self.is_credit else '-') \
               + str(self.quantity) + ' on date: ' + str(self.created_date_time)
