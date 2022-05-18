from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("", views.student_show, name="student_show"),
    path('redirect/', views.data_flair),
    path('dataflair/', views.index, name="index"),
    path('djangotutor/', views.Tutorial.as_view()),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.show_cookie),
    path('delete_cookie/', views.delete_cookie),
    path('testcookie/', views.cookie_session),
    path('deletecookie/', views.cookie_delete),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('delete/', views.delete_session),
    path('form/', views.registration_form, name='registration_form'),
    path('base/', views.home, name='homepage'),
    path('other/', views.other, name='other_page'),
    path('about/', views.about, name='about'),
]
