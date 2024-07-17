from django.shortcuts import render, redirect
from web.models import Student
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "app/index.html")
def hello(request, name):
    context = {"name": name}
    return render(request, "app/hello.html", context)
    
def call(request):
    all_students = Student.objects.all()
    context = {"data": all_students}
    return render(request, "app/student.html", context)

def newstudent(request):
    if request.method == "POST":
        name= request.POST.get ("first")
        regNo= request.POST.get ("second")
        DOB= request.POST.get ("third")
        CGPA= request.POST.get ("forth")
        if not name or not regNo or not DOB or not CGPA:
            messages.error(request, "All fields are required")
            return redirect(newstudent)
        new_student= Student.objects.create(name= name, reg_number= regNo, cgpa= CGPA)
        new_student.save()
        messages.success(request, "created successfully")
        return redirect (home)
    return render(request, "app/newstudent.html")

def school(request):
    return render(request, "app/festus.html")
