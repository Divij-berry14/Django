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


def set_cookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    if request.COOKIES.get("visits"):
        html.set_cookie('dataflair', "Welcome Back")
        value = int(request.COOKIES.get("visits"))
        html.set_cookie("visits", value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie("visits", value)
        html.set_cookie("dataflair", text)
    return html


def show_cookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse(
            "<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/student/set_cookie/')


def delete_cookie(request):
    if request.COOKIES.get("visits"):
        response = HttpResponse("<h1>dataflair<br>Cookie deleted</h1>")
        response.delete_cookie("visits")
    else:
        response = HttpResponse("<h1>dataflair</h1>need to create cookie before deleting")
    return response
