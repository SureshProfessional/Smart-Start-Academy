from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("info/",views.info,name="info"),    

    path("school-page/",views.school_page,name="school_page"),    

    path("add-subject/",views.add_subject,name="add_subject"),
    path("all-subject/",views.all_subject,name="all_subject"),

    path("add-std/",views.add_std,name="add_std"),
    path("all-std/",views.all_std,name="all_std"),
    path("delete-std/<str:id>",views.delete_std,name="delete_std"),




]
