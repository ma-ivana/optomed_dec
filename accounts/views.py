from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user
from .decorators import allowed_users
from .decorators import admin_only
from django.contrib.auth.models import Group


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='secretaria')
            user.groups.add(group)

            messages.success(request, 'Account was creater for ' + username)
            return redirect('accounts:login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if username == 'secretaria':
                return redirect('accounts:indexsecretaria')
            elif username == 'profmed':
                return redirect('accounts:indexprofmed')
            elif username == 'ventas':
                return redirect('accounts:indexventas')
            elif username == 'taller':
                return redirect('accounts:indextaller')
            elif username == 'gerencia':
                return redirect('accounts:indexgerencia')

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')


def adm(request):
    return render(request, 'accounts/adm.html')


def home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'secretaria'])
def indexsecretaria(request):
    return render(request, 'accounts/indexsecretaria.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'profmed'])
def indexprofmed(request):
    return render(request, 'accounts/indexprofmed.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'ventas'])
def indexventas(request):
    return render(request, 'accounts/indexventas.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'taller'])
def indextaller(request):
    return render(request, 'accounts/indextaller.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'gerencia'])
def indexgerencia(request):
    return render(request, 'accounts/indexgerencia.html')


def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)
