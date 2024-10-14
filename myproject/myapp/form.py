from django import forms
from myapp.models import Student

# class StudentForm(forms.Form):
#     FirstName=forms.CharField(max_length=20)
#     LastName=forms.CharField(max_length=20)
#     Contact=forms.IntegerField()

class EmpForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"