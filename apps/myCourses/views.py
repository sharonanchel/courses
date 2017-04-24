from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
        "courses" : Course.objects.all()
        }
    return render(request, "myCourses/index.html", context)

def courses(request):
    Course.objects.create(course=request.POST['name'],
    description=request.POST['description'])
    return redirect('/')

def delete(request, id):
    Course.objects.filter(id=id).delete()
    return render(request, "myCourses/delete.html")
