from django.shortcuts import render
from .serializers import StocktickSerializer, UpdateStocktickSerializer
from .models import Stocktick
from rest_framework.views import APIView
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.


class StockticklistView(ListModelMixin, GenericAPIView):
    queryset = Stocktick.objects.all()
    serializer_class = StocktickSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


class StocktickView(UpdateModelMixin, GenericAPIView):
    queryset = Stocktick.objects.all()
    serializer_class = UpdateStocktickSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

# class Stockupdate(APIView):
#     def patch(self,request,pk,format=None):
#         id=pk
#         stu = Stocktick.objects.get(pk=id)
#         serializer = StocktickSerializer(stu,data=request.data,partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'data':serializer.data
#             })
#         return Response(serializer.errors)
