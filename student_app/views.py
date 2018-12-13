from django.shortcuts import render
from student_app.models import Student

# Create your views here.
def index(request):
	students = Student.objects.all().order_by('id')
	return render(request, 'index.html', context={'students': students })

def details(request, student_id):
	student = Student.objects.get(id=student_id)
	return render(request, 'details.html', context={'student': student })


