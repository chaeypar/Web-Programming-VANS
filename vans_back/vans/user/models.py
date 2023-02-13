from django.db import models
import secrets
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid
GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

def generate_hex(nbytes=32):
    return secrets.token_hex(nbytes)

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an emmai address")
        user = self.model(
            emil=self.normalize_email(email),
        )
        user.ser_password(password)
        user.save(using=self._db)  
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    """
    [User Model]
    """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          null=False, blank=False, auto_created=True)
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    # profile_image = models.ImageField(null=True, blank=True)
    
    is_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    # campany 
    
    
    # client_user
    shipping_name = models.CharField(max_length=20, null=True, blank=True)
    shipping_phone_number = models.CharField(
        max_length=11, null=True, blank=True)
    shipping_zipcode = models.CharField(max_length=10, null=True, blank=True)
    shipping_address1 = models.CharField(max_length=100, null=True, blank=True)
    shipping_address2 = models.CharField(max_length=100, null=True, blank=True)
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.email} ({self.nickname})"
    
class AuthToken(models.Model):
    id = models.CharField(default=generate_hex,
                          max_length=64, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)