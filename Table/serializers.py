from rest_framework import serializers
from .models import Stocktick


class StocktickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocktick
        fields = '__all__'


class UpdateStocktickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocktick
        fields = ['Pcase']
