from http.client import HTTPResponse
from msilib.schema import ListView
from pickle import TRUE
from re import template
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BookForm
from Table.models import Stocktick
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from Table.serializers import StocktickSerializer
from . serializers import RemarkstocktickSerializer
from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Count
# from django.db.models import Avg, Count, Min, Sum
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate
from . serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from . permissions import IsOwner
from rest_framework import status
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

# views


def ShowPage(request, pk):
    all_data = Stocktick.objects.filter(Godown=pk)
    gData = Stocktick.objects.values('Godown').distinct()
    # print(all_data)

    if request.method == "GET":
        Godown_filter = request.GET.get('selected_Godown')
        all_data = Stocktick.objects.filter(Godown=Godown_filter)
        # print(Godown_filter)
        return render(request, 'stock/table.html', {'key1': all_data, 'key2': gData, 'search': Godown_filter})

# for update data


def updatedata(request):
    status = Stocktick.objects.filter(Status=True).update(Status=False)
    # return render(request, 'stock/table.html', {'key1':status})
    return redirect(reverse('showpage', args=(1,)))

# for single data fetch


class Get_stock_List(APIView):
    def get_object(self, pk):
        try:
            return Stocktick.objects.get(pk=pk)
        except Stocktick.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StocktickSerializer(snippet)
        return Response(serializer.data)

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


# just for practice data model main


class DropDown(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get(self, request, format=None):
        current_user = request.user.id
        
        if request.user.groups.filter(name='stockistHO').exists():
            isHigher = True
        elif request.user.groups.filter(name='rawtea').exists():
            isHigher1 = True
            return render(request, 'stock/higher.html', {'isHigher1': isHigher1})
        else:
            isHigher = False
            
        if self.request.method == "GET" and 'selected_Godown' in request.GET:
            gData = Stocktick.objects.values(
                'Godown').distinct().exclude(Godown='B')
            # print(gData)
            Godown_filter = request.GET.get('selected_Godown')
            # print(Godown_filter)
            all_data = Stocktick.objects.filter(Godown=Godown_filter)
            
            total_case = Stocktick.objects.filter(
                Godown=Godown_filter).aggregate(Sum('Cases')).get('Cases__sum')
            # print(total_case)

            total_p_case = Stocktick.objects.filter(
                Godown=Godown_filter).aggregate(Sum('Pcase'))
            p = total_p_case['Pcase__sum']

        else:
            gData = Stocktick.objects.values(
                'Godown').distinct().exclude(Godown='B')
            # print(gData)
            # print(gData[0])
            all_data = Stocktick.objects.filter(Godown=gData[0]['Godown'])
            total_case = Stocktick.objects.filter(
                Godown=gData[0]['Godown']).aggregate(Sum('Cases')).get('Cases__sum')
            print(total_case)
            total_p_case = Stocktick.objects.filter(
                Godown=gData[0]['Godown']).aggregate(Sum('Pcase'))
            p = total_p_case['Pcase__sum']
            Godown_filter = gData[0]['Godown']

        return render(request, 'stock/table.html', {'key1': all_data, 'key2': gData, 'sum': total_case, 'case': p, 'selected': Godown_filter, 'isHigher': isHigher, 'current_user':current_user})


# templates
def higher(request):
    if request.user.groups.filter(name='higher').exists():
        isHigher = True
        return render(request, 'stock/higher.html', {'isHigher': isHigher})
        # current_user_groups = request.user.groups.values_list("name", flat=True)
        # print(current_user_groups)
    else:
        isHigher = False
        return render(request, 'stock/lower.html', {'isHigher': isHigher})


# for remarks api
# class RemarksView(UpdateModelMixin, GenericAPIView):
#     queryset = Stocktick.objects.all()
#     serializer_class = RemarkstocktickSerializer

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

# for upate data by current user

class StockUpdate(GenericAPIView, UpdateModelMixin):
    serializer_class = RemarkstocktickSerializer
    queryset = Stocktick.objects.all()
    
    
    def patch(self, request, *args, **kwargs):
        print(request.data)
        return self.partial_update(request, *args, **kwargs)
    
    
# for filter
class Get_All_stock_List(generics.ListAPIView):
    queryset = Stocktick.objects.all()
    serializer_class = StocktickSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Godown']


# values match views
# for duplicate row
# class DuplicateRow(APIView):
#     sum_cases = 0
#     for row in Stocktick.objects.values('OurLot').distinct():
#         # print(row)
#         matched_value = Stocktick.objects.filter(OurLot__exact=row['OurLot'])[
#             1:].values_list('id', flat=True)
#         # print(matched_value)
#         total_cases = Stocktick.objects.filter(OurLot__exact=row['OurLot'])[
#             1:].aggregate(Sum('Cases'))
#         # print(total_cases)
#         sum_cases = total_cases['Cases__sum']
#         Stocktick.objects.filter(OurLot__exact=row['OurLot']).update(Cases=sum_cases)
#         # Stocktick.objects.filter(pk__in=list(matched_value)).delete()

#         # Stocktick.objects.filter(OurLot__exact=row['OurLot']).update(Cases=sum_cases)
#         # print(case)

#         # print(sum_cases)
#         # Stocktick.objects.filter(OurLot__exact=row['OurLot']).update(Cases=sum_cases)
#         # Stocktick.objects.filter(pk__in=list(matched_value)).update(Cases=sum_cases)

#         total_sum = Stocktick.objects.filter(OurLot__exact=row['OurLot']).aggregate(Sum('Cases'))
    # print(total_sum)

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({'msg': 'LogOut'}, status=status.HTTP_200_OK)
