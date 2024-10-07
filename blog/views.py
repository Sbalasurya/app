from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    #return HttpResponse("Hello from index page")
    return render(request,"index.html")

def detail(request, post_id):
    return HttpResponse(f"You are viewing details page and id is {post_id}")

def old_url(request):
    return redirect(reverse('blog:new_page_url'))

def new_url(request):
    return HttpResponse("This is the new url")