from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(School)
admin.site.register(Std)
admin.site.register(Subject)