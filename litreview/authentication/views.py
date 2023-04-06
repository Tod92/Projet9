from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from authentication import forms

from feed.forms import AvatarPicForm
# Create your views here.



def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})



@login_required
def upload_profile_photo(request):
    photo_form = AvatarPicForm()
    if request.method == 'POST':
        user = request.user
        photo_form = AvatarPicForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo = photo_form.save(commit=False)
            photo.user = request.user
            photo.save()
            user.profile_photo = photo
            user.save()
            return redirect('feed')
    return render(request, 'authentication/upload_profile_photo.html', context ={'form': photo_form})



# def signup_page(request):
#     signup_form = forms.SignupForm()
#     profile_picture_form = forms.UploadProfilePhotoForm()
#     if request.method == 'POST':
#         signup_form = forms.SignupForm(request.POST)
#         profile_picture_form = forms.UploadProfilePhotoForm(request.POST, request.FILES)
#         if all([signup_form.is_valid(), profile_picture_form.is_valid()]):
#             user = signup_form.save()
#             profile_picture_form.save(commit=False)
#             # auto-login user
#             login(request, user)
#             return redirect(settings.LOGIN_REDIRECT_URL)
#     context = {
#         'signup_form': signup_form,
#         'profile_picture_form': profile_picture_form,
#     }
#     return render(request, 'authentication/signup.html', context=context)
