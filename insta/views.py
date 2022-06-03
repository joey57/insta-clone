import re
from django.shortcuts import redirect, render
from django.http  import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm 

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for  {username}')
            return redirect('login.html')
    else:
       form = UserRegisterForm()
    return render(request, 'users/register.html',{"form":form})