from django.shortcuts import render
from rest_framework import viewsets
from .models import Webapp
from .serializers import WebappSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# Declatation of quuery set from models

class WebappView(viewsets.ModelViewSet):
	queryset = Webapp.objects.all()
	serializer_class = WebappSerializer
	filter_backends = (SearchFilter, OrderingFilter)
	ordering_fields = ('clicks', 'date', 'revenue') # ascending or descending 
	search_fields = ('date', 'channel', 'os', 'country')  # grouping by columns

	def ger_queryset(self):
		queryset = self.queryset.extra(select = {cpi:spend/installs})
		return queryset