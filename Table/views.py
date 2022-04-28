from django.shortcuts import render
from .serializers import StocktickSerializer, UpdateStocktickSerializer
from .models import Stocktick
from rest_framework.views import APIView
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
import requests
# Create your views here.


class StockticklistView(ListModelMixin, GenericAPIView):
    queryset = Stocktick.objects.filter()
    serializer_class = StocktickSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


class StocktickView(UpdateModelMixin, GenericAPIView):
    queryset = Stocktick.objects.all()
    serializer_class = UpdateStocktickSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
