from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .decorator import logout_required

@logout_required
def home(request):
    return render(request,"index.html")

@logout_required
def about(request):
    return render(request,"about.html")

@logout_required
def contact(request):
    return render(request,"contact.html")

def info(request):
    return render(request,"info.html")

@logout_required
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = SchoolRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "SCHOOL"
            user.save()
            School.objects.create(user=user)
            messages.success(request,"School created successfully!")
            return redirect("/login")
    else:
        form =  SchoolRegisterForm()
    return render(request,"register.html",{"form":form})

@logout_required
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            
            user = authenticate(email=email,password=password)
            if user is not None:
                if user.is_staff == True:
                    messages.info(request,"you are admin you cannot login here!")
                    return redirect("/login")                    
                else:
                    login(request,user)
                    return redirect("/profile")
            else:
                messages.error(request,"Email and Password is invalid")
                return redirect("/login")
                
    else:
        form = LoginForm()
    return render(request,"login.html",{"form":form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("/")    

@login_required
def profile(request):    
    user = request.user
    school = getattr(user,"school",None)
    
    if request.method == "POST":
        user_form = Profile(request.POST,request.FILES,instance=user)
        school_form = SchoolProfile(request.POST,request.POST,instance=school)
        
        if user_form.is_valid() and school_form.is_valid():
            user_form.save()
            if user.role == "SCHOOL":
                school_form.save()
                messages.success(request,"Profile updated successfully")
                return redirect("/profile")
        
    else:
        user_form = Profile(instance=request.user)
        school_form = SchoolProfile(instance=school)
        
    return render(request,"profile.html",{
        "user_form":user_form,
        "school_form":school_form,
    })

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
    return render(request,"school_page.html",context)


@login_required
def add_student(request):    
    print(request)
    if request.user.role != "SCHOOL":
        print(request.user.role)
        messages.error(request, "You are not allowed to add students.")
        return redirect("/")
    
    if request.method == "POST":
        print(request.POST)
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
                return redirect("/all-student")
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
    print(students)
    return render(request,"all_student.html",{"students":students})
    
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
    print(std)
    return render(request,"all_std.html",{"stds":std})

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
    return render(request,"all_subject.html",{"subjects":subjects})