from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser

# -----------------------------------------------
# Custom User (Base for all roles)
# -----------------------------------------------
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(("email address"), unique=True)
    
    ROLE = (
        ('SCHOOL', 'SCHOOL'),
        ('TEACHER', 'TEACHER'),
        ('STUDENT', 'STUDENT'),
        ('PARENT', 'PARENT'),
    )
    role = models.CharField(choices=ROLE, max_length=50)
    
    # Common details
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to="upload", blank=True, null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.role}"
