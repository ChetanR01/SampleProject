from django.shortcuts import render, HttpResponse, redirect
from .models import Students

# Create your views here.
def index(request):
    return HttpResponse('<h1> Hello </h1>')

def students(request):
    students= Students.objects.filter(is_active=True)
    print('Students Tbl Records = ', students)
    return render(request, 'student-table.html', {"students":students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_no= request.POST['roll_no']
        div = request.POST['div']
        city=request.POST['city']
        mobile_no = request.POST['mobile_no']

        Students.objects.create(name=name, roll_no=roll_no, class_div = div, city=city, mobile_no=mobile_no)
        return redirect('/students')


    return render(request, 'add-student.html',{})