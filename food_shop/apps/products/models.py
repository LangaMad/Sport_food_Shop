from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField('Категории')
    code = models.UUIDField(unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name