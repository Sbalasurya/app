from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello from index page")

def detail(request):
    return HttpResponse("You are viewing details page")