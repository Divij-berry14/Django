from django.shortcuts import render
from . import forms

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_profile(request):
    form = forms.ProfileForm()
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split(".")[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile_maker/errors.html')
            user_pr.save()
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form}
    return render(request, 'profile_maker/create.html', context)
