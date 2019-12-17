from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework import authentication, permissions
from .models import *
from rest_framework import pagination
from rest_framework import viewsets
# Create your views here.

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    """
    Creating just for testing the token and user authentication module
    Will edit it later on
    """
    def get(self, request):
        content = {
            'message': 'Hello, World'
        }
        return Response(content)

class HomeView(APIView):
    """
    View to list of all the wallpaper used for the home
    Requires token authentication
    Only admin user are able to access this views
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes     = (IsAuthenticated, )
    def get(self, request, format=None):
        """
        Return a list of wallpaper used for home page
        """
        return_json = { }
        
        """
        Segment for latest wallpaper of homepage
        """
        latest_wallpaper_obj = Wallpaper.objects.all().order_by('-created_at')
        latest_wallpaper_json = []
        for wallpaper in latest_wallpaper_obj:
            latest_wallpaper_value = {
                'id': wallpaper.id,
                'cat_id': wallpaper.category.id,
                'wallpaper_image': settings.WEB_URL + wallpaper.image.url,
                'wallpaper_image_thumb': settings.WEB_URL + wallpaper.thumbnail.url,
                'total_views': wallpaper.total_views,
                'total_rate': wallpaper.rate_avg,
                'wall_tags': [tag.slug for tag in wallpaper.tags.all()],
                'cid': wallpaper.category.id,
                'category_name': wallpaper.category.name,
                'category_image': settings.WEB_URL +  wallpaper.category.image.url,
                'category_image_thumb': settings.WEB_URL +  wallpaper.category.image.url
            }
            latest_wallpaper_json.append(latest_wallpaper_value)
        return_json.update({'latest_wallpaper': latest_wallpaper_json})
        
        """
        Segment for most viewed wallpaper
        """
        most_viewed_obj = Wallpaper.objects.all().order_by('-total_views')
        most_viewed_json = []
        for wallpaper in most_viewed_obj:
            most_viewed_value = {
                'id': wallpaper.id,
                'cat_id': wallpaper.category.id,
                'wallpaper_image': settings.WEB_URL +  wallpaper.image.url,
                'wallpaper_image_thumb': settings.WEB_URL +  wallpaper.thumbnail.url,
                'total_views': wallpaper.total_views,
                'total_rate': wallpaper.rate_avg,
                'wall_tags': [tag.slug for tag in wallpaper.tags.all()],
                'cid': wallpaper.category.id,
                'category_name': wallpaper.category.name,
                'category_image': settings.WEB_URL + wallpaper.category.image.url,
                'category_image_thumb': settings.WEB_URL +  wallpaper.category.image.url
            }
            most_viewed_json.append(most_viewed_value)
        return_json.update({'most_viewed_wallpaper': most_viewed_json})

        """
        Segment for most rated wallpaper
        """
        most_rated_obj = Wallpaper.objects.all().order_by('-rate_avg')
        most_rated_json = []
        for wallpaper in most_rated_obj:
            most_rated_value = {
                'id': wallpaper.id,
                'cat_id': wallpaper.category.id,
                'wallpaper_image': settings.WEB_URL +  wallpaper.image.url,
                'wallpaper_image_thumb': wallpaper.thumbnail.url,
                'total_views': wallpaper.total_views,
                'total_rate': wallpaper.rate_avg,
                'wall_tags': [tag.slug for tag in wallpaper.tags.all()],
                'cid': wallpaper.category.id,
                'category_name': wallpaper.category.name,
                'category_image': settings.WEB_URL +  wallpaper.category.image.url,
                'category_image_thumb': wallpaper.category.image.url
            }
            most_rated_json.append(most_rated_value)
        return_json.update({'most_rated_wallpaper': most_rated_json})

        return Response({'HD_WALLPAPER': return_json})

class LargeResultPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page'
    max_page_size = 1

class LatestWallpaper(viewsets.ModelViewSet):

    pagination_class = LargeResultPagination
    """
    Fetching all the latest wallpaper with any limit and showing 
    into part part
    """
    def list(self, request):
        """
        Return a list of wallpaper used for home page
        """
        return_json = { }
        
        """
        Segment for latest wallpaper of homepage
        """
        latest_wallpaper_obj = Wallpaper.objects.all().order_by('-created_at')
        latest_wallpaper_json = []
        for wallpaper in latest_wallpaper_obj:
            latest_wallpaper_value = {
                'id': wallpaper.id,
                'cat_id': wallpaper.category.id,
                'wallpaper_image': settings.WEB_URL + wallpaper.image.url,
                'wallpaper_image_thumb': settings.WEB_URL + wallpaper.thumbnail.url,
                'total_views': wallpaper.total_views,
                'total_rate': wallpaper.rate_avg,
                'wall_tags': [tag.slug for tag in wallpaper.tags.all()],
                'cid': wallpaper.category.id,
                'category_name': wallpaper.category.name,
                'category_image': settings.WEB_URL +  wallpaper.category.image.url,
                'category_image_thumb': settings.WEB_URL +  wallpaper.category.image.url
            }
            latest_wallpaper_json.append(latest_wallpaper_value)        
        return Response({'HD_WALLPAPER': latest_wallpaper_json})