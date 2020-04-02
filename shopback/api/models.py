from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)

    def to_json(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count
        }