from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'latest_wallpaper', LatestWallpaper, base_name='latest_wallpaper')
urlpatterns = router.urls

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('home_wallpaper/', HomeView.as_view(), name='home_wallpaper'),
    path('latest_wallpaper/', LatestWallpaper.as_view({'get': 'list'}))

]
