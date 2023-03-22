from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
   return HttpResponse("Hello <strong> Im Lubna </strong> and this is my first trial with django")

# Create your views here.
