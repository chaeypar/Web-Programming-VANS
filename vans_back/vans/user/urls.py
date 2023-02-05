from django.urls import path
from .views import UserSignUp, UserLogin

urlpatterns = [
    path('signup', UserSignUp.as_view()),
    path('signin', UserLogin.as_view())
]
