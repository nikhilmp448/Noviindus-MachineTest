
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True,blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="image/product")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'item'
        verbose_name_plural = 'item'

    def save(self, *args, **kwargs) :
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    


