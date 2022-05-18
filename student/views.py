from .models import Student
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.urls import reverse
from . import forms


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
        response = HttpResponse("<h1>data flair<br>Cookie deleted</h1>")
        response.delete_cookie("visits")
    else:
        response = HttpResponse("<h1>data flair</h1>need to create cookie before deleting")
    return response


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>data flair</h1>")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("data flair<br> cookie created")
    else:
        response = HttpResponse("Data flair <br> Your browser does not accept cookies")
    return response


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>data flair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of data flair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('/student/create/')


def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>data flair<br>Session Data cleared</h1>")


def registration_form(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'We have received this form again!'
        if form.is_valid():
            html = html + "The Form is Valid"
    else:
        html = 'welcome for first time'
    return render(request, 'sign_up.html', {'html': html, 'form': form})


def home(request):
    return render(request, 'base.html')


def other(request):
    context = {'k1': 'Welcome to the Second page'}
    return render(request, 'others.html', context)