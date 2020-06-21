from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name = "index"),
    path('start', views.home, name = "h`ome"),
    path('time', views.time, name = "time")
]