from django.db import models
from django.contrib import admin

class Shop(models.Model):
    name = models.CharField(verbose_name="商品名", max_length=10)
    money = models.IntegerField(verbose_name="金額")
    note = models.CharField(verbose_name="備考", max_length=10, default="", blank=True)

    def __str__(self):
        return self.name


admin.site.register(Shop)