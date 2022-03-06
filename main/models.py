from django.db import models

from main.querysets.shops import ShopsQuerySet


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_workers'


class Shop(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey('main.Worker', models.CASCADE, 'shops')

    objects = ShopsQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_shops'


class Visit(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey('main.Shop', models.CASCADE, 'visits')
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.datetime.__str__()

    class Meta:
        db_table = 'main_visits'
