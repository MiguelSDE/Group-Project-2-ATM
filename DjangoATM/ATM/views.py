from django.shortcuts import render
from .forms import CardSignupForm

# Create your views here.
def index(request):
    return render(request, 'ATM/index.html')

def signup(request):
    form = CardSignupForm()
    context = {'form':form}
    return render(request, 'ATM/signup.html', context)

