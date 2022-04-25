from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from . serializers import UserSerializer, PostSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from . models import Post
from rest_framework import permissions
from . permissions import IsOwner
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, CreateModelMixin


# Create your Register views here.
# Registeruserview


class UserRegister(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
# login view


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'})
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


# for crud in all

class BlogModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):  # delete
        print(self.request.user.id)
        serializer.save(updated_by=self.request.user)


# views for create data


# class PostBlog(CreateModelMixin, generics.GenericAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)


# # get all data


# class ListBlogs(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

#     def get(self, request, format=None):
#         blog = Post.objects.all()
#         serializer = PostSerializer(blog, many=True)
#         print(serializer.data)
#         return Response({
#             'status': 'All Data',
#             'data': serializer.data
#         })
# # update data


# class UpdateBlog(UpdateModelMixin, generics.GenericAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def perform_update(self, serializer):  # delete
#         print(self.request.user.id)
#         serializer.save(updated_by=self.request.user)


# # Delete Data


# class DestroyBlog(DestroyModelMixin, generics.GenericAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
# # Logout user


class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({'msg': 'LogOut'}, status=status.HTTP_200_OK)


# for update sceond method
# class UpdateBlog(viewsets.ModelViewSet):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def perform_update(self, serializer):  #delete
#         print(self.request.user.id)
#         serializer.save(updated_by=self.request.user)

# for second method to create post
# class PostBlog(viewsets.ModelViewSet):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)
