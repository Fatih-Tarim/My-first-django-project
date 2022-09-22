 #from django.http.response import HTTPResponse


from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "blog/index.html")

def blogs(request):
    return render(request, "blog/blogs.html")

def blog_details(request, id):
    return render(request, "blog/blog-details.html",{
        "id":id 
    })