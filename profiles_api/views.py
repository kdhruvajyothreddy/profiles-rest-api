from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your '
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
