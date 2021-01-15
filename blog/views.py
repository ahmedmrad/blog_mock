from django.shortcuts import render, redirect
from .forms import UserForm, AuthorsProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "blog/index.html")


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = AuthorsProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # hash the password
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user  # relating one to one relationship
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = AuthorsProfileInfoForm()
    return render(
        request, 'blog/register.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        }
    )


def user_login(request):
    if request.method == ' POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('Login failed')
                return HttpResponse('Invalid login details')
    else:
        return render(request, 'blog/user_login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))


def about(request):
    return render(
        request,
        'blog/about.html',
    )
