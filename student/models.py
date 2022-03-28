from django.db import models


class Student(models.Model):
    roll_number = models.TextField()
    name = models.TextField(max_length=40)
    stud_class = models.TextField()
    department = models.TextField()

    def __str__(self):
        return self.roll_number

