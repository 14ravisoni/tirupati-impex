from django.db import models

from .abstract_attributes import DateTimeAbstract


WORKER_TYPES_CHOICES = (('jadai', 'jadai'), ('ghaat', 'ghaat'))


class Worker(DateTimeAbstract):
    first_name = models.CharField(max_length=100, blank=True, default="")
    middle_name = models.CharField(max_length=100, null=True, default="")
    last_name = models.CharField(max_length=100, null=True, default="")
    nick_name = models.CharField(max_length=100, blank=False, default=first_name)
    profile_pic = models.CharField(max_length=300, null=True, default="")
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    worker_type = models.CharField(max_length=10, choices=WORKER_TYPES_CHOICES, blank=False, null=False, default='Jadai')

    def __str__(self):
        return self.first_name + self.last_name + ' (' + self.nick_name + ')'


class WorkerStoneRate(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    diamond = models.IntegerField(blank=True, null=True)
    navratna = models.IntegerField(blank=True, null=True)
    pink_ruby = models.IntegerField(blank=True, null=True)


class WorkerStats(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    acceptance_count = models.IntegerField(null=True, blank=True, default=0)
    rejection_count = models.IntegerField(null=True, blank=True, default=0)
    current_count = models.IntegerField(null=True, blank=True, default=0)
    pending_count = models.IntegerField(null=True, blank=True, default=0)
    completed_count = models.IntegerField(null=True, blank=True, default=0)
    current_metal_amount = models.DecimalField(max_digits=10, null=True, decimal_places=3)
    total_metal_count = models.DecimalField(max_digits=10, null=True, decimal_places=3)
    average_rating = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
