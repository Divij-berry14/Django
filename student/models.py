from django.db import models
from django.urls import reverse


class Student(models.Model):
    roll_number = models.TextField()
    name = models.TextField(max_length=40)
    stud_class = models.TextField()
    department = models.TextField()

    def __str__(self):
        return self.name

    '''PyCharm proposes this because the method does not use self in its body and 
    hence does not actually change the class instance. Hence the method could be static,
    i.e. callable without passing a class instance or without even having created a class instance.'''
    @staticmethod
    def get_absolute_url():
        return reverse('student:student_show')
