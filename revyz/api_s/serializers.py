from rest_framework import serializers
from .models import api_s

class api_sSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_s
        fields = ('id','Name', 'Address', 'City', 'Number', 'Email', 'Tech_skill')