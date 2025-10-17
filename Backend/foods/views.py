from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import search_food

class FoodSearchAPIView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        if not query:
            return Response({'error': 'Query requerida'}, status=400)
        data = search_food(query)
        return Response(data)