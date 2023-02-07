from django.db import models

class Product(models.Model):
    user = models.ForeignKey('user.User', related_name="products")