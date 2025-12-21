from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib.auth.decorators import login_required
from main_app.decorator import logout_required
from main_app.models import School
from django.contrib import messages

@logout_required
def register(request):
    if request.method == "POST":        
        form = SchoolRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "SCHOOL"
            user.save()
            School.objects.create(user=user)
            messages.success(request,"School created successfully!")
            return redirect("/auth/login")
    else:
        form =  SchoolRegisterForm()
    return render(request,"main_file/register.html",{"form":form})

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
                    return redirect("/auth/login")                    
                else:
                    login(request,user)
                    return redirect("/auth/profile")
            else:
                messages.error(request,"Email and Password is invalid")
                return redirect("/auth/login")
                
    else:
        form = LoginForm()
    return render(request,"main_file/login.html",{"form":form})

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
                return redirect("/auth/profile")
        
    else:
        user_form = Profile(instance=request.user)
        school_form = SchoolProfile(instance=school)
        
    return render(request,"main_file/profile.html",{
        "user_form":user_form,
        "school_form":school_form,
    })

