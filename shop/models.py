from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Бренд')
    description = models.CharField(max_length=255, verbose_name='Опис')
    image = models.ImageField(upload_to='brands/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категорія')
    position = models.SmallIntegerField(unique=False, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, verbose_name='Опис')
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.name

class Line(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Лінія')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, verbose_name='Опис')
    image = models.ImageField(upload_to='lines/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, db_index=True)
    brnd = models.ForeignKey(Brand, on_delete=models.PROTECT)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, verbose_name='Опис')
    articul = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    properties = models.TextField(blank=True, verbose_name='Характеристики')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна')
    popular = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
