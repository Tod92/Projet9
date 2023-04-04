from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from authentication import forms

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

@login_required
def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm()
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES,instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('feed')
    return render(request, 'authentication/upload_profile_photo.html', context ={'form': form})
