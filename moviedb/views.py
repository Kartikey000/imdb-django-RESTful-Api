from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
# Create your views here.

class movieList(APIView):

	def get(self,request):
		ob = Movie.objects.all()
		serializer = MovieSerializer(ob, many=True)
		return Response(serializer.data, status=200)

