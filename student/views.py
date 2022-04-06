from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def student_show(request):
    student = Student.objects.order_by('roll_number')
    return render(request, 'student_show.html', {'student': student})
