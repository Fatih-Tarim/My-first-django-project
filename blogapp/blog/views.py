from http.client import HTTPResponse
from msilib.schema import LockPermissions
from django.shortcuts import render, HttpResponse

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Kurs1",
            "image": "1.png",
            "is_active": True,
            "is_home": True,
            "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quidemminus nulla nobis odit blanditiis numquam!"
        },
        {
            "id": 2,
            "title": "Kurs2",
            "image": "1.png",
            "is_active": True,
            "is_home": True,
            "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quidemminus nulla nobis odit blanditiis numquam!"
        },
        {
            "id": 3,
            "title": "Kurs3",
            "image": "1.png",
            "is_active": True,
            "is_home": False,
            "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quidemminus nulla nobis odit blanditiis numquam!"
        },
    ]
}


def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    # blogs = data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog

    blogs = data["blogs"]
    selectedBlog = [blog for blog in blogs if blog["id"]==id][0]

    return render(request, "blog/blog-details.html", {
        "blog": selectedBlog
    })
