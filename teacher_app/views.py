from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from main_app.decorator import logout_required

@login_required
def add_teacher(request):
    school = get_object_or_404(School,user=request.user)
    if request.method == "POST":
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.school = school
            subject.save()
            return redirect("/all-subject")
    else:
        form = AddTeacherForm()     
               
    context = {
        "form": form,
        "form_title": "Add Teacher",
        "form_icon": "bi bi-person-plus-fill",
        "submit_text": "Add Teacher",
        "submit_icon": "bi bi-person-plus",
        "date_fields": ["dob", "admission_date"],
    }
    return render(request,"add_universal_form.html",context)
