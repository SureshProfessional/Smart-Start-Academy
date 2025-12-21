from main_app.forms import BaseIndianForm,IndianDateInput
from django import forms
from teacher_app.models import Teacher

class AddTeacherForm(BaseIndianForm):    
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Teacher
        fields = ["std","subject","join_date","experience","qualification"]
        widgets = {
            "join_date": IndianDateInput(),            
        }
    field_order = [        
        "email",
        "first_name",
        "last_name",
        "std",
        ]