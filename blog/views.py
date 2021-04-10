from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    name= "<html><body> Welcome to my blog page</body></html>" 
    return HttpResponse(name)
        
