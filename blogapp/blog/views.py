 #from django.http.response import HTTPResponse


from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("hoempage")

def blogs(request):
    return HttpResponse("Blogs")

def blog_details(request, id):
    return HttpResponse("blog details:"+str(id))