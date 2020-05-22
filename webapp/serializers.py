from rest_framework import serializers
from .models import Webapp

class WebappSerializer(serializers.ModelSerializer):
	class Meta:
		model = Webapp
		fields = ('id', 'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend',  'revenue')