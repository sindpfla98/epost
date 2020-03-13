from rest_framework import serializers
from .models import CallingPlan

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallingPlan
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallingPlan
        fields = '__all__'