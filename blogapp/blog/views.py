from http.client import HTTPResponse
from msilib.schema import LockPermissions
from django.shortcuts import render, HttpResponse
from blog.models import Blog

data = {

}


def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True)
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    # blogs = data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog

    # blogs = data["blogs"]
    # selectedBlog = [blog for blog in blogs if blog["id"]==id][0]

    blog = Blog.objects.get(id=id)

    return render(request, "blog/blog-details.html", {
        "blog": blog
    })
