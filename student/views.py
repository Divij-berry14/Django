from .models import Student
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.urls import reverse


def index(request):
    return HttpResponse("<h1>Data Flair Django</h1>Hello, you just configured your First URL")


def data_flair(request):
    # return HttpResponseRedirect(reverse('index'))
    # return HttpResponseRedirect("/student/dataflair")
    return redirect('/student/dataflair')


class Tutorial(RedirectView):
    url = 'https://data-flair.training/blogs/category/django/'


def student_show(request):
    student = Student.objects.order_by('roll_number')
    return render(request, 'student_show.html', {'student': student})
