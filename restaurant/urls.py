from django.urls import path
from .views import *

urlpatterns = [
    path("menu/", menu, name="menu"),
    path("", home, name="home"),
    path("about/", about, name="about"),
    # path("book/", book, name="book"),
    path("menu/dish/<str:name>", dish)
]