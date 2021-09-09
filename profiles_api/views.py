from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you more control over your application logic',
            'Is mapper mannually to URLs',
        ]

        return Response({'message': 'hello world', 'an_apiview': an_apiview})
