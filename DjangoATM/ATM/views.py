from django.shortcuts import render
from django.contrib import messages
from .forms import CardSignupForm

# Create your views here.
def index(request):
    return render(request, 'ATM/index.html')

def signup(request):
    form = CardSignupForm()
    text = ""
    if request.method ==  'POST':
        form = CardSignupForm(request.POST)
        if form.is_valid():
            text = "A new ATM card has been added to your account."
            form.save()
    
    context = {'form':form,'text':text}
    return render(request, 'ATM/signup.html', context)






