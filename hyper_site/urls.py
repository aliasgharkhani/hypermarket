from django.contrib import admin
from django.urls import path, include
from hyper_site.views import *

urlpatterns = [
    path('home/', home)
]
