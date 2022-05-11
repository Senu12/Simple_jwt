from rest_framework import serializers
from .models import Stocktick


class StocktickSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stocktick
        fields = '__all__'
        

    # def update(self, instance, validated_data):
    #     print("===============",instance)
    #     instance.Remarks = validated_data.get('Remarks', instance.Remarks)
    #     # instance.content = validated_data.get('content', instance.content)
    #     # instance.created = validated_data.get('created', instance.created)
    #     return instance


class UpdateStocktickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocktick
        fields = ['Pcase']
