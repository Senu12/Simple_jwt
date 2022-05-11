from rest_framework import serializers
from Table.models import Stocktick
from django.contrib.auth.models import User

class ValueSerializer(serializers.ModelSerializer):
    Status = serializers.SerializerMethodField()

    def get_Status(self, obj):
        if obj.Status == True:
            return False

    class Meta:
        model = Stocktick
        fields = '__all__'
        
# register serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class RemarkstocktickSerializer(serializers.ModelSerializer):
    # updated_by = serializers.ReadOnlyField(source='updated_by.username')
    
    class Meta:
        model = Stocktick
        fields = ['Remarks','updated_by']