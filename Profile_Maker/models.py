from django.db import models


class UserProfile(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    technologies = models.CharField(max_length=500)
    email = models.EmailField(default=None)
    display_picture = models.FileField()
    """display_picture is a File Field. It should have been an image field. 
    We use a file field to store files on the server. 
    It will create a File object which has many built-in attributes and methods. 
    When a user uploads a file in the file field, we are storing file object in database 
    and store file in MEDIA_ROOT. """

    def __str__(self):
        return self.f_name
