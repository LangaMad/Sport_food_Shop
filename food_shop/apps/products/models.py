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
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Фото', upload_to='products/')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name



