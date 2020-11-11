from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib import messages
from django import forms

from .models import*

class CreateAccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput()) 
    class Meta: 
        model = Account
        fields=('account_name','password', 'confirm_password')

    
    def clean(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

class CardSignupForm(ModelForm):
    class Meta:
        model = Card
        fields = ('card_name','account_number', 'balance', 'address', 'phone_number')
        
     
        
 

   
    