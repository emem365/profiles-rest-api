from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you more control over your application logic',
            'Is mapper mannually to URLs',
        ]

        return Response({'message': 'hello world', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hellow messgae with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello { name }'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update an object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a list of Features"""
        a_viewset = [
            'Uses Actions (list, create, update, retrieve, partial_update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello world', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'Hello { name }'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve Object"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Update Object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Partial update Object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Delete Object"""
        return Response({'http_method':'DELETE'})
