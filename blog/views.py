from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_blog(request):
    return render(request, "blog/blog.html")