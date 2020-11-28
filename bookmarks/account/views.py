from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile

# Create your views here.

# Display Dashboard
@login_required
def dashboard(request):
    template = 'account/dashboard.html'
    context = {
        'section': 'dashboard'
    }
    return render(request, template, context)


# User Authentication and Login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        context = {
            'form': form,
            }
        return render(request, 'account/login.html', context)


# USER REGISTRATION
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html", {'new_user': new_user})
        
    else:
        user_form =UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})



