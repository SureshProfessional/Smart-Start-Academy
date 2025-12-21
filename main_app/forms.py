from django import forms
from .models import *
from student_app.models import Student
from teacher_app.models import Teacher


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
    


    
class AddStdForm(forms.ModelForm):
    class Meta: 
        model = Std
        fields = ["std","div","room_no"]

class AddSubjectForm(forms.ModelForm):
    class Meta: 
        model = Subject
        fields = ["std","name","code","description"]
        
