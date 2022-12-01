from django.shortcuts import render,redirect
from django.views import *
from .models import *
from .forms import *
# Create your views here.

class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html', {'studata':stu_data})

class Add_student(View):
    def get(self,request):
        fm = AddStudentForm()
        return render(request, 'core/add-student.html', {'form':fm})

    def post(self,request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-student.html', {'form':fm})


class delete_Student(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')