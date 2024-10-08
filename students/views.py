from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, "students/index.html", {
        'Students': Student.objects.all()
    })
    
def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid:
            new_student = form.save(commit=False)
            new_student.save()
            
            return render(request, 'students/add.html', {
                'form' : StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
            
    return render(request, 'students/add.html', {
        'form' : StudentForm()
    })
    
def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid:
            form.save()
            return render(request, 'students/edit.html', {
                'form' : StudentForm(),
                'success': True
            })
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })
    

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))