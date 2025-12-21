from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorator import logout_required

@logout_required
def home(request):
    return render(request,"main_file/index.html")

@logout_required
def about(request):
    return render(request,"main_file/about.html")

@logout_required
def contact(request):
    return render(request,"main_file/contact.html")

def info(request):
    return render(request,"main_file/info.html")

@login_required
def school_page(request):
    school = request.user.school
    all_student = len(Student.objects.filter(school=school))
    all_teacher = len(Teacher.objects.filter(school=school))
    all_subject = len(Subject.objects.filter(school=school))
    all_std = len(Std.objects.filter(school=school))

    context = {        
        "all_student":all_student,
        "all_teacher":all_teacher,
        "all_subject":all_subject,
        "all_std":all_std,
    }
    return render(request,"school/school_page.html",context)

@login_required    
def add_std(request):
    school = get_object_or_404(School,user=request.user)
    if request.method == "POST":
        form = AddStdForm(request.POST)
        if form.is_valid():
            std = form.save(commit=False)
            std.school = school
            std.save()
            messages.success(request,"Class added successfully")
            return redirect("/all-std")
    else:
        form = AddStdForm()
    context = {
        "form": form,
        "form_title": "Add New STD",
        "form_icon": "bi bi-person-plus-fill",
        "submit_text": "Add STD",
        "submit_icon": "bi bi-person-plus",
        "date_fields": ["dob", "admission_date"],
    }
    return render(request,"add_universal_form.html",context)

@login_required    
def all_std(request):
    std = Std.objects.filter(school=request.user.school).order_by("std")    
    return render(request,"school/all_std.html",{"stds":std})

@login_required
def delete_std(request,id):
    if request.method == "POST":
        std = get_object_or_404(Std,id=id)
        std.delete()
        return redirect("all_std")
    return redirect("all_std")

@login_required
def add_subject(request):
    school = get_object_or_404(School,user=request.user)
    if request.method == "POST":
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.school = school
            subject.save()
            return redirect("/all-subject")
    else:
        form = AddSubjectForm()     
               
    context = {
        "form": form,
        "form_title": "Add Subject",
        "form_icon": "bi bi-person-plus-fill",
        "submit_text": "Add STD",
        "submit_icon": "bi bi-person-plus",
        "date_fields": ["dob", "admission_date"],
    }
    return render(request,"add_universal_form.html",context)
            

@login_required    
def all_subject(request):
    subjects = Subject.objects.filter(school=request.user.school)    
    return render(request,"school/all_subject.html",{"subjects":subjects})

