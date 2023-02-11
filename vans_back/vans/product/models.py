from django.db import models

class Product(models.Model):
    name = models.CharField()
    # images 
    price = models.PositiveIntegerField()
    discount_rate = models.PositiveSmallIntegerField() # %단위 표기
    delivery_cost = models.PositiveIntegerField()
    inventory_by_size = models.JSONField()
    
    num = models.PositiveIntegerField()
    status = models.Choices()
    manufacturer = models.CharField()
    model_code = models.CharField()
    manufacturing_date = models.DateField()
    origin = models.CharField()
    extra_info = models.JSONField()
    description = models.TextField()
    tags = models.JSONField()
    
    
    