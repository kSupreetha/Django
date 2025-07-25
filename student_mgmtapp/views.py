from django.shortcuts import render, redirect, get_object_or_404
from .models import student

def home(request):
    return render(request, 'student_mgmtapp/home.html')

def student_list(request):
    student = student.objects.all()
    return render(request, 'student_mgmtapp/student_list.html', {'student_mgmtapp': student})

def add_student(request):
    if request.method == 'POST':
        student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            roll_no=request.POST['roll_no'],
            course=request.POST['course']
        )
        return redirect('student_list')
    return render(request, 'student_mgmtapp/add_student.html')

def edit_student(request, id):
    student = get_object_or_404(student, id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.roll_no = request.POST['roll_no']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'student_mgmtapp/edit_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(student, id=id)
    student.delete()
    return redirect('student_list')
