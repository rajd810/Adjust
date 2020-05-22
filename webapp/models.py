from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


# Field thats going to used in admin database.

class Webapp(models.Model):
	date = models.DateField(auto_now=False,auto_now_add=False)
	channel = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	os = models.CharField(max_length = 100)
	impressions = models.CharField(max_length = 100)
	clicks = models.CharField(max_length = 100)
	installs = models.CharField(max_length = 100)
	spend = models.CharField(max_length = 100)
	revenue = models.CharField(max_length = 100)

	def __str__(self):
		return self.channel
