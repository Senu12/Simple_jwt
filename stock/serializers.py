from rest_framework import serializers
from Table.models import Stocktick

class ValueSerializer(serializers.ModelSerializer):
    Status = serializers.SerializerMethodField()

    def get_Status(self, obj):
        if obj.Status == True:
            return False

    class Meta:
        model = Stocktick
        fields = '__all__'