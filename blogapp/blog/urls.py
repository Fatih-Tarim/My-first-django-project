# http://127.0.0.1:8000/

from importlib.resources import path
from django.urls import path
from . import views

urlpatterns =[
    path("", views.index),
    path("index", views.index),
    path("blogs", views.blogs),
    path("blogs/<int:id>", views.blog_details)
]