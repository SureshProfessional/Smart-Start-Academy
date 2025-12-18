from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class IndianDateInput(forms.DateInput):
    format = '%d-%m-%Y'

    def __init__(self, **kwargs):
        kwargs['format'] = self.format
        kwargs['attrs'] = {'class': 'crm-date', 'autocomplete': 'off'}
        super().__init__(**kwargs)

class BaseIndianForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                field.input_formats = ["%d-%m-%Y", "%Y-%m-%d"]

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
    
class AddStudentForm(BaseIndianForm):    
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Student
        fields = ["std","gr_no","dob","admission_date","caste","blood_group","parent_contact"]
        widgets = {
            "dob": IndianDateInput(),
            "admission_date": IndianDateInput(),
        }
    field_order = [
        "gr_no",
        "email",
        "first_name",
        "last_name",
        "std",
        ]

    
class AddStdForm(forms.ModelForm):
    class Meta: 
        model = Std
        fields = ["std","div","room_no"]

class AddSubjectForm(forms.ModelForm):
    class Meta: 
        model = Subject
        fields = ["std","name","code","description"]