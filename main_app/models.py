from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager


# -----------------------------------------------
# Custom User (Base for all roles)
# -----------------------------------------------
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    
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


# ------------------------------------------------------------------
# school    
# ------------------------------------------------------------------    

class School(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    school_code = models.CharField(max_length=20,null=True,blank=True,unique=True)
    established_year = models.PositiveIntegerField(blank=True,null=True)    
    contact_number = models.CharField(max_length=15,null=True,blank=True)
    website = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.school_name

# ------------------------------------------------------------------
# Standard (class)
# ------------------------------------------------------------------    

class Std(models.Model):
    std = models.CharField(max_length=10)
    div = models.CharField(max_length=5,null=True,blank=True)
    room_no = models.CharField(max_length=10,null=True,blank=True)
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="standards")
    
    
    def __str__(self):
        return f"{self.std} - {self.div or ''}"
    
# ------------------------------------------------------------------
# Subject
# ------------------------------------------------------------------    

class Subject(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="subjects")
    std = models.ForeignKey(Std,on_delete=models.CASCADE,related_name="subjects")
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10,null=True,blank=True)
    description = models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return f"{self.name} ({self.std})"
    
# ------------------------------------------------------------------
# Teacher
# ------------------------------------------------------------------
    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="teachers")
    std = models.ForeignKey(Std,on_delete=models.SET_NULL,null=True,blank=True,related_name="class_teacher")
    subject = models.ManyToManyField(Subject,blank=True,related_name="teachers")
    
    salary = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    join_date = models.DateField(blank=True,null=True)
    experience = models.PositiveIntegerField(help_text="Years of experience",blank=True,null=True)
    qualification = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return f"{self.user.first_name} ({self.school.school_name})"

# ------------------------------------------------------------------
# Student
# ------------------------------------------------------------------
    
class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="students")
    std = models.ForeignKey(Std,on_delete=models.CASCADE,related_name="students")
    
    gr_no = models.CharField(max_length=20,unique=True)
    roll_no = models.PositiveIntegerField(null=True,blank=True)
    admission_date = models.DateField(blank=True,null=True)
    caste = models.CharField(choices=(("SC","SC"),("ST","ST"),("OBC","OBC"),("GENERAL","GENERAL")),max_length=50)
    dob = models.DateField(blank=True,null=True)
    blood_group = models.CharField(max_length=5,blank=True,null=True)
    parent_contact = models.CharField(max_length=15,blank=True,null=True)
    
    def __str__(self):
        return f"{self.user.first_name} ({self.std})"
    
# ------------------------------------------------------------------
# Parent
# ------------------------------------------------------------------

class Parent(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="parents")
    children = models.ManyToManyField(Student,related_name="parents")
    occupation = models.CharField(max_length=100,blank=True,null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    contact_number = models.CharField(max_length=15,blank=True,null=True)
    
    def __str__(self):
        return f"{self.user.first_name} ({self.school.school_name})"
    