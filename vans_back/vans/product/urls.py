from django.urls import path
from .views import ProductCreateList, ProductDetail

urlpatterns = [
    path('products', ProductCreateList.as_view()),
    path('products/<str:pk>', ProductDetail.as_view())
]
