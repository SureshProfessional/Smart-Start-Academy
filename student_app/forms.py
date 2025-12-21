from django import forms
from main_app.forms import IndianDateInput,BaseIndianForm
from .models import Student

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