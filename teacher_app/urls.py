from django.urls import path
from . import views

urlpatterns = [
    path("add-student/",views.add_teacher,name="add_teacher"),
    # path("all-student/",views.all_student,name="all_student"),
]