from django.db import models
from django.contrib import admin


class Shop(models.Model):
    name = models.CharField(verbose_name="商品名", max_length=10, default="")
    money = models.IntegerField(verbose_name="金額", default=0)
    size = models.IntegerField(verbose_name="大きさ", default=0)
    quantity = models.IntegerField(verbose_name="個数", default=0)
    color = models.CharField(verbose_name="色", max_length=10, default="")
    date = models.CharField(verbose_name="日付", max_length=20, default="")
    sold = models.CharField(verbose_name="売り切れ", max_length=10, default="")
    note = models.CharField(verbose_name="備考", max_length=10, default="", blank=True)

    def __str__(self):
        return self.name


admin.site.register(Shop)
