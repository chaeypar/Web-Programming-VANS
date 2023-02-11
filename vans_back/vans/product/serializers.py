from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ("name", "price", "discount_rate", "delivery_cost", " inventory_by_size",
                  "num", "status", "manufacturer", "model_code", "manufacturing_date",
                  "origin", "extra_info", "description", "tags", "id")
        read_onry_field = ("id")