from django.urls import path
from . import views


urlpatterns = [
    path('room', views.Room_View.as_view())
]
