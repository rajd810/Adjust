from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


# Field thats going to used in admin database.

class Webapp(models.Model):
	date = models.DateField(
		verbose_name = "Date"
	)
	channel = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	os = models.CharField(max_length = 100)
	impressions = models.PositiveIntegerField()
	clicks = models.PositiveIntegerField()
	installs = models.PositiveIntegerField()
	spend = models.PositiveIntegerField()
	revenue = models.PositiveIntegerField()

	class Meta:
		verbose_name = "Webapp"
		verbose_name_plural = "Webapp"

	def __str__(self):
		return self.channel
