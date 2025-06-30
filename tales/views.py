from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import Tale
from .forms import TaleForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def list_tales(request):
    tales = Tale.objects.all()
    return render(request, 'tales/list_tales.html', {'tales': tales})

def landing_page(request):
    return render(request, 'tales/landing_page.html')

def error_404(request, exception):
    return render(request, 'tales/landing_page.html')

@login_required
def add_tale(request):
    if not request.user.groups.filter(name='AdminTales').exists():
        return HttpResponseForbidden("No tienes acceso a esta página")
    if request.method == "POST":
        form = TaleForm(request.POST, request.FILES)
        print(form.is_valid())
        print(form.errors)
        
        if form.is_valid():
            form.save()
            return redirect('../list')
    else:
        form = TaleForm()
    return render(request, 'tales/add_tale.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            nombre_del_grupo = 'UsersTales'
            grupo = Group.objects.get(name=nombre_del_grupo)
            user.groups.add(grupo)


            auth_login(request, user)  
            return redirect('landing_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})