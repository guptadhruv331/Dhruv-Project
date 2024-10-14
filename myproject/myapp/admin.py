from django.contrib import admin
from .models import Student

class StudentData(admin.ModelAdmin):
    list_display=["First_Name","Age","Contact"]

admin.site.register(Student,StudentData)
# Register your models here.
