from django.db import models
from auth_app.models import CustomUser
from django.utils.translation import gettext_lazy as _

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
    