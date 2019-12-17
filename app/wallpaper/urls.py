from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('home_wallpaper/', HomeView.as_view(), name='home_wallpaper')
]
