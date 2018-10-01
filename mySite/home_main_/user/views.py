from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , get_user_model
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse
from django.views.generic import CreateView
from .forms import RegisterForm,SubscribersForm
from django import forms
# from .forms import signupForm
from social_django.models import UserSocialAuth

# @login_required
# def home(request):
#     return render(request,'index.html',)

User =get_user_model()

def signup_page(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return render(request, 'index.html',)

    # if request.method == 'POST':
    #     form = signupForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         # mobile = form.cleaned_data.get('mobile')
    #         # stucomp = form.cleaned_data.get('stucomp')
    #         user = authenticate(username=username,password = password)
    #         login(request,user)
    #         # return redirect('home')
    #         form.save()
    else:
        form = RegisterForm(request.POST)
    return render(request, 'registration/signup.html' ,{'form':form})



def login_page(request):
    return render(request, 'registration/login.html' ,)

# @login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, '/registration/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

# @login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, '/registration/password.html', {'form': form})

def Subscriber(request):
    if request.method == "POST":
        form =SubscribersForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return render(request, 'index.html',)
    else:
        form = RegisterForm(request.POST)
    return render(request, 'index.html' ,{'form':form})