from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length= 150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', null=True)

    def __str__(self):
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']

class Product(models.Model):
    product_name = models.CharField(max_length= 150, verbose_name='наименование')
    description = models.TextField(verbose_name= 'описание', null= True)
    img = models.ImageField(verbose_name= 'изображение', upload_to='images/', blank=True, null=True)
    category = models.CharField(verbose_name= 'категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(verbose_name= 'дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name= 'дата последнего изменения', auto_now_add=True)
    group = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name']


