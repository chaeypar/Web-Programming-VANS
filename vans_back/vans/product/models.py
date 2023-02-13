import uuid
from django.db import models

CATEGORY_CHOICES = [
        ('T', '티셔츠'),
        ('S', '신발'),
        ('O', '기타'),
    ]

FEATURED_CHOICES = [
    ('C', "코어클래식"),
    ('O', "올드스쿨"),
    ('M', "뮬 패밀리"),
    ('S', "스케이트 클래식"),
    ('F', "CUMFYCUSH"),
    ('A', "애너하임 팩토리")
]

KIDS_CHOICES = [
    ('T', "토들러"),
    ('K', "키즈")
]

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    ]

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          null=False, blank=False, auto_created=True)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="S")
    featured = models.CharField(max_length=1, choices=FEATURED_CHOICES, null=True, blank=True)
    kids = models.CharField(max_length=1, choices=KIDS_CHOICES, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    is_new = models.BooleanField(default=False)
    
    name = models.CharField(max_length=100, null=False, blank=False)
    # images 
    price = models.PositiveIntegerField(null=False, blank=False)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2) # %단위 표기
    delivery_cost = models.PositiveIntegerField()
    
    num = models.PositiveIntegerField()
    # status = models.Choices()
    manufacturer = models.CharField(max_length=20)
    model_code = models.CharField(max_length=20, null=True, blank=True)
    manufacturing_date = models.DateField()
    origin = models.CharField(max_length=20)
    extra_info = models.JSONField(null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    tags = models.JSONField(default=[])
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
# class Inventory(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                           null=False, blank=False, auto_created=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="inventorys")
#     name = models.CharField(max_length=30, null=False, blank=False)
    
    
    
class InventoryItem(models.Model):
    size
    