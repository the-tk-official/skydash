from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm, ProfileForm
from users.models import Profile


# Create your views here.

def loginForMentor(request):
    if request.user.is_authenticated:
        return redirect('accounts')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            prof = user.profile.prof
            if prof == 'Mentor':
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('accounts')
                else:
                    messages.error(request, 'Password is incorrect!')
            else:
                messages.error(request, "You're not mentor!")
        except:
            messages.error(request, "Username does not exist!")
    return render(request=request, template_name='users/login.html')


@login_required(login_url='login')
def logoutMentor(request):
    logout(request)

    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('accounts')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request=request, template_name='users/register.html', context=context)


@login_required(login_url='login')
def update(request, pk):
    profile = Profile.objects.get(id=pk)
    pk = profile.id

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'pk': pk
    }

    return render(request=request, template_name='users/update.html', context=context)


@login_required(login_url='login')
def delete(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()

    return redirect('accounts')
