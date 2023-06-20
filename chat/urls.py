# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("room/", views.RoomView.as_view(), name="room"),
]
