from django.db import models
from main_app.models import CustomUser,School,Std,Subject

# ------------------------------------------------------------------
# Teacher
# ------------------------------------------------------------------
    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=10,unique=True)        
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="teachers")
    std = models.ForeignKey(Std,on_delete=models.SET_NULL,null=True,blank=True,related_name="class_teacher")
    subject = models.ManyToManyField(Subject,blank=True,related_name="teachers")    
    salary = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    join_date = models.DateField(blank=True,null=True)
    experience = models.PositiveIntegerField(help_text="Years of experience",blank=True,null=True)
    qualification = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return f"{self.user.first_name} ({self.school.school_name})"
