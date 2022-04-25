from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers
from . models import Post
from rest_framework.authtoken.models import Token

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

# POST SERIALIZERS


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content',
                  'picture', 'created_by', 'updated_by']

    def create(self, validated_data):
        print(("===================",validated_data))
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.picture = validated_data['picture']
        instance.updated_by = validated_data['updated_by']
        instance.save()
        return instance


# class OwnerSerializer(serializers.ModelSerializer):
#     post = serializers.StringRelatedField(many=True)
#     # post = serializers.PrimaryKeyRelatedField(
#     #     many=True, queryset=Post.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'post']

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = OwnerSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsOwner]
