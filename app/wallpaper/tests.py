from django.test import TestCase

# Create your tests here.
from .models import Wallpaper

class WallpaperTestCase(TestCase):
    def setup(self):
        Wallpaper.objects.create()
        pass