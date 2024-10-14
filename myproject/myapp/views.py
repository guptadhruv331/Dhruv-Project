from django.shortcuts import render
from myapp.form import EmpForm
# from myapp.form import StudentForm

from django.http import HttpResponse

from django.template import loader

def index12(request):
    temp=loader.get_template('Home.html')
    return HttpResponse(temp.render())

def index11(request):
    temp=loader.get_template('contact.html')
    return HttpResponse(temp.render())

def index10(request):
    temp=loader.get_template('about.html')
    return HttpResponse(temp.render())

# def index90(request):
#     student=StudentForm()
#     return render(request,"index.html",{'form':student})

def index9(request):
    stu=EmpForm()
    return render(request,"index.html",{'form':stu})


# def index9(request):
#     temp=loader.get_template('index.html')
#     return HttpResponse(temp.render())

# def index10(request):
#     temp=loader.get_template('Simar.html')
#     return HttpResponse(temp.render())

# def index11(request):
#     temp=loader.get_template('Rupinder.html')
#     return HttpResponse(temp.render())


# def index(request):
#     return HttpResponse("<h1>Hi, Good Morning.</h1>")
# def index2(request):
#     return HttpResponse("<h1>Hi, My Name is Dhruv.</h1>")
# def index3(request):
#     return HttpResponse("<h1>I recently completed my Senior Secondary Education from C.B.S.E Board.</h1>")
# def index4(request):
#     return HttpResponse("<h1>I am from Ambala City.</h1>")

# def abc(request):
#     temp=loader.get_template('index.html')
#     return HttpResponse(temp.render())