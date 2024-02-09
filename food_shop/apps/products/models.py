from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Категории',max_length=50,unique=True)
    slug = models.SlugField('Слаг')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField('Подкатегории', max_length=50, unique=True)
    slug = models.SlugField('Слаг')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Одежда', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)





    def __str__(self):
        return self.name