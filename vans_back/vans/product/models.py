import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          null=False, blank=False, auto_created=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    # images 
    price = models.PositiveIntegerField(null=False, blank=False)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2) # %단위 표기
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
    
    
    