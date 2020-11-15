from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

from .models import*

class CreateAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username','password1', 'password2',)


class CardSignupForm(ModelForm):
    class Meta:
        model = Card
        fields = ('balance', 'issue_date',
        'exp_date','address', 'phone_number',)
        
     
 

   
    