from django.db import models
from main_app.models import CustomUser,School,Std


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
    