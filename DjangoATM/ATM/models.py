from django.db import models
from datetime import datetime, timedelta

# Create your models here.

# Makes a database for ATM account
class Account(models.Model):
    account_name = models.CharField(max_length=30)  
    account_number = models.PositiveIntegerField() 
    issue_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    #might needs this
    #timestamp = models.DateField(auto_now_add=False, auto_now=False, blank=True) 
    exp_date = models.DateField(default=datetime.now() + timedelta(days=1095))
    balance = models.PositiveIntegerField() 
    #not sure about the correct way to do this (status based on cardblock request/exp. date)
    #card_status = ???
    address = models.CharField(max_length=60)  
    phone_number = models.PositiveIntegerField()  

   
    




