from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("info/",views.info,name="info"),

    path("register/",views.register,name="register"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),

    path("profile/",views.profile,name="profile"),

    path("school-page/",views.school_page,name="school_page"),

    path("add-student/",views.add_student,name="add_student"),
    path("all-student/",views.all_student,name="all_student"),

    path("add-subject/",views.add_subject,name="add_subject"),
    path("all-subject/",views.all_subject,name="all_subject"),

    path("add-std/",views.add_std,name="add_std"),
    path("all-std/",views.all_std,name="all_std"),




]
