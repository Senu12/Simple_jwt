from rest_framework import serializers
from .models import Stocktick, TeaBag

# For Nested serializer
class TeaBagSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeaBag
        fields = ['PacketId']
        

class NewSerializer(serializers.ModelSerializer):

    Ourlot = TeaBagSerializer(many=True)

    class Meta:
        model = Stocktick
        fields = (
            'OurLot',
            'Ourlot'
        )


# To get data by id
class StocktickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stocktick
        fields = '__all__'


# for update data
class UpdateStocktickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocktick
        fields = ['Pcase']


# for updated_by_id
class RemarkstocktickSerializer(serializers.ModelSerializer):
    # updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Stocktick
        fields = ['Remarks', 'updated_by']
