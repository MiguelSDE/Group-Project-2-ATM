from django.db import models
from django import forms
from datetime import datetime, timedelta

# Create your models here.

class Account(models.Model):
    account_name = models.CharField(max_length=30) 
    
    def __str__(self):
        return self.account_name 

# Makes a database for ATM card
class Card(models.Model):
    card_name = models.CharField(max_length=30)  
    account_number = models.PositiveIntegerField() 
    issue_date = models.DateField(auto_now_add=False, auto_now=False, blank=False, null=True)
    #might needs this
    #timestamp = models.DateField(auto_now_add=False, auto_now=False, blank=True) 
    exp_date = models.DateField(default=datetime.now() + timedelta(days=1095))
    balance = models.PositiveIntegerField() 
    #not sure about the correct way to do this (status based on cardblock request/exp. date)
    card_status = "Active"
    address = models.CharField(max_length=60)  
    phone_number = models.PositiveIntegerField()  

    def __str__(self):
        return self.card_name
   
    




