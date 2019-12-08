from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_products')

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    cname = models.CharField('Series', max_length=200, db_index=True)
    pname = models.CharField('Products', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True,
                            help_text='모델명, 제조사, 키워드 등을 조합하여 띄어 쓰기(공란) 없이 입력합니다. (공란은 "_"를 이용)')

    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True)
    related_url = models.TextField(blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField('Meta', blank=True)

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    unit_price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']]

    def __str__(self):
        return "[ " + self.cname + " | " + self.pname + " | " + self.created.strftime(
            "%Y-%m-%d %H:%M:%S" + " ]")

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])