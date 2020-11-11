from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
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
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login')
        else:
            messages.error(request, 'Passwords must contain at least 8 characters and must match')
    context = {'form':form, 'text':text}
    return render(request, 'ATM/index.html', context)
    

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(request, username = username, password = password)
        # if account is valid, logs it in
        if account is not None:
            login(request, account)
            return redirect('/account-panel')
        else:
            messages.error(request, 'Username OR Password is incorrect')

    return render(request, 'ATM/login.html')

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





