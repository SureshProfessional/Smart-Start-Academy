from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from main_app.decorator import logout_required

@login_required
def add_student(request):        
    if request.user.role != "SCHOOL":        
        messages.error(request, "You are not allowed to add students.")
        return redirect("/")
    
    if request.method == "POST":        
        form = AddStudentForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            
            if CustomUser.objects.filter(email=email).exists():
                form.add_error("email","Email already exist")
                
            else:
                user = CustomUser.objects.create(email=email,first_name=first_name,last_name=last_name,role="STUDENT")
                
                user.set_unusable_password()
                user.save()
                
                student = form.save(commit=False)
                student.user = user
                student.school = request.user.school
                student.save()
                
                messages.success(request,f"{first_name} added successfully")
                return redirect("/students/all-student")
    else:
        form = AddStudentForm()
        
    context = {
        "form": form,
        "form_title": "Add New Student",
        "form_icon": "bi bi-person-plus-fill",
        "submit_text": "Add Student",
        "submit_icon": "bi bi-person-plus",
        "date_fields": ["dob", "admission_date"],
    }
    return render(request,"add_universal_form.html",context)

@login_required    
def all_student(request):
    students = Student.objects.filter(school=request.user.school).order_by("gr_no")    
    return render(request,"students/all_student.html",{"students":students})
    
@login_required    
def delete_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":        
        student.delete()
        return redirect("all_student")
    return redirect("all_student")
        