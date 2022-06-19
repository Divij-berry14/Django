from django import forms
from .models import UserProfile

"""
Model forms
The basic concept of model forms is that they derive their structure from models. 
Yes, that’s right, we don’t have to define a form and connect it with models. We can do that directly via model forms.

Models forms are a subclass of forms. When we make a form using ModelForm class, we use META class.
 In META, there are two attributes required, they are:
1. model: It takes in the name of the model. We have to import the User_Profile model for this. 
This attribute defines the model to render a form. 
This form object is then used to save the user data to be stored directly in a database.

2. fields: It is a list of strings. This list will take the name of the fields in the model. 
This field defines input fields for a form. We specify the fields from models in this list. 
All the fields mentioned in this list will be used to create a form.
"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['f_name', 'l_name', 'technologies', 'email', 'display_picture']
