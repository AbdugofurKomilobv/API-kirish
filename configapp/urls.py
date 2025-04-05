from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # movie get, post
    path('movie_api/',movie_api),
    # movie get,put,patch
    path('movie_detail/<slug:slug>/', movie_detail),
    # actors_api get,post
    path('actor_api/',actor_api),

    #actor_detail  get,put,patch,delete 
    path('actor_detail/<int:pk>/',actor_detail),
]