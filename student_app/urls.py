from django.urls import path
from . import views

urlpatterns = [
    path("add-student/",views.add_student,name="add_student"),
    path("all-student/",views.all_student,name="all_student"),
    path("delete-student/<str:id>",views.delete_student,name="delete_student"),
]