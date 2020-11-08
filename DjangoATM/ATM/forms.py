from django.forms import ModelForm
from .models import Account

class CardSignupForm(ModelForm):
    class Meta:
        model = Account
        fields = {'account_name', 'account_number', 'balance', 'address', 'phone_number'}