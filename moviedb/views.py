from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .serializers import MovieSerializer
# Create your views here.

class BasicPagination(PageNumberPagination):
	page_size_query_param='limit'

class movieList(APIView):
	
	pagination_class = BasicPagination
	serializer_class = MovieSerializer

@property
def paginator(self):
	if not hasattr(self, '_paginator'):
		if self.pagination_class is None:
			self.paginator = None
		else:
			self._paginator = self.pagination_class()
	else:
		pass
	return self._paginator



def paginate_queryset(self, queryset):

	if self.paginator is None:
		return None
	return self.paginator.paginate_queryset(queryset, self.request, view=self)

   
def get_paginated_response(self, data):
	assert self.paginator is not None
	return self.paginator.get_paginated_response(data)


def get(self, request, format=None, *args, **kwargs):

	ob = Movie.objects.all()
	page = self.paginate_queryset(ob)
	if page is not None:
		serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
		#serializer = self.serializer_class(ob, many=True)


	else:
		serializer=self.serializer_class(ob, many=True)

	return Response(serializer.data, status=200)




