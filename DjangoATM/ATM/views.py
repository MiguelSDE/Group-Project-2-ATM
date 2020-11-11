from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import*

from .models import*

# Create your views here.
def index(request):
    form = CreateAccountForm()
    text = ""
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            text = "Account created."
            form.save()
            return redirect('/login')
        else:
            text = "Account name already exists or passwords don't match."
    context = {'form':form, 'text':text}
    return render(request, 'ATM/index.html', context)
    

def log_in(request):
    if request.method == 'POST':
        account_name = request.POST.get('account_name')
        password = request.POST.get('password')
        user = authenticate(request, account_name = account_name, password = password)

        login(request, user)
        return redirect('/account-panel')
    
    context = {}
    return render(request, 'ATM/login.html', context)

def add_card(request):
    form = CardSignupForm()
    text = ""
    if request.method == 'POST':
        form = CardSignupForm(request.POST)
        if form.is_valid():
            text = "A new ATM card has been added to your account."
            form.save()
    context = {'form':form,'text':text}
    return render(request, 'ATM/add-card.html', context)

def account_panel(request):
    context = {}
    return render(request, 'ATM/account-panel.html', context)





