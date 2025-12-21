from django.contrib.auth.forms import UserCreationForm
from django import forms
from auth_app.models import CustomUser
from main_app.models import School

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