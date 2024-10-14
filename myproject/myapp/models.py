from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name= models.CharField(max_length=20)
    Contact=   models.IntegerField()
    Email=     models.EmailField(max_length=50)
    Age=       models.IntegerField()
    new_image= models.FileField(upload_to="new/",max_length=500,null=True,default=None)
    
    class Meta:
        db_table="Student"


# Create your models here.
