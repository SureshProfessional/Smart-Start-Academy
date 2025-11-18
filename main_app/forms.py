from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class SchoolRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email","password1","password2"]

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
class Profile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["photo","first_name","email","address","city","state","pincode"]
        
class SchoolProfile(forms.ModelForm):
    class Meta:
        model = School
        fields = ["school_name","established_year","contact_number","website"]
    
class AddStudentForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    class Meta:
        model = Student
        fields = ["std","gr_no","roll_no","dob","admission_date","caste","blood_group","parent_contact"]
        widgets = {
            "admission_date": forms.DateInput(attrs={"type": "date"}),
            "dob": forms.DateInput(attrs={"type": "date"}),
        }

    
class AddStdForm(forms.ModelForm):
    class Meta: 
        model = Std
        fields = ["std","div","room_no"]

class AddSubjectForm(forms.ModelForm):
    class Meta: 
        model = Subject
        fields = ["std","name","code","description"]