from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
