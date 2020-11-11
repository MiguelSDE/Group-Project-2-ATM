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

        def clean(self):
            cleaned_data = super(CreateAccountForm, self).clean()

            password = cleaned_data.get('password1')
            password_confirm = cleaned_data.get('password2')

            if password and password_confirm:
                if password != password_confirm:
                    raise forms.ValidationError("The two password fields must match.")
            return cleaned_data


class CardSignupForm(ModelForm):
    class Meta:
        model = Card
        fields = ('card_name','account_number', 'balance', 'address', 'phone_number')
        
     
        
 

   
    