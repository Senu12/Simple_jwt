from optparse import Values
from django.shortcuts import render
from Table.models import Stocktick, TeaBag
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from Table.serializers import StocktickSerializer, TeaBagSerializer, NewSerializer,RemarkstocktickSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import never_cache

# for single data fetch

class Get_stock_List(APIView):
    def get_object(self, pk):
        try:
            return Stocktick.objects.get(pk=pk)
        except Stocktick.DoesNotExist:
            raise status.Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StocktickSerializer(snippet)
        return Response(serializer.data)


# Dropdown and fetch data 
decorators = [never_cache, ]

@method_decorator(decorators, name='dispatch')
class DropDown(LoginRequiredMixin, APIView):
    login_url = '/login/'

    def get(self, request, format=None):
        current_user = request.user.id

        if request.user.groups.filter(name='stockistHO').exists():
            isHigher = True
        elif request.user.groups.filter(name='rawtea').exists():
            isHigher1 = True
            return render(request, 'stock/higher.html', {'isHigher1': isHigher1})
        else:
            isHigher = False
         
        # selecting from dropdown
        if self.request.method == "GET" and 'selected_Godown' and 'row_no' in request.GET:
            gData = Stocktick.objects.values('Godown').distinct().exclude(Godown='B')            
            Godown_filter = request.GET.get('selected_Godown') 
            row_data = Stocktick.objects.filter(Godown=Godown_filter).values('RowNo').distinct()           
            Row_filter = request.GET.get('row_no')                         
            all_data = Stocktick.objects.filter(Godown=Godown_filter,RowNo=Row_filter)
            total_case = Stocktick.objects.filter(Godown=Godown_filter,RowNo=Row_filter).aggregate(Sum('Cases')).get('Cases__sum')
            total_p_case = Stocktick.objects.filter(Godown=Godown_filter,RowNo=Row_filter).aggregate(Sum('Pcase'))
            p = total_p_case['Pcase__sum']
            
        else:
            print('hello')
            gData = Stocktick.objects.values('Godown').distinct().exclude(Godown='B')
            row_data = Stocktick.objects.filter(Godown=gData[0]['Godown']).values('RowNo').distinct()
            all_data = Stocktick.objects.filter(Godown=gData[0]['Godown'],RowNo=row_data[0]['RowNo'])           
            # for sum
            total_case = Stocktick.objects.filter(Godown=gData[0]['Godown'],RowNo=row_data[0]['RowNo']).aggregate(Sum('Cases')).get('Cases__sum')            
            total_p_case = Stocktick.objects.filter(Godown=gData[0]['Godown'],RowNo=row_data[0]['RowNo']).aggregate(Sum('Pcase'))
            p = total_p_case['Pcase__sum']
            Godown_filter = gData[0]['Godown']
            Row_filter = row_data[0]['RowNo']
            print(Godown_filter)
            print(Row_filter)

        return render(request, 'stock/table.html', {'key1': all_data, 'key2': gData, 'key3': row_data,'sum': total_case, 'case': p, 'selected': Godown_filter, 'row':Row_filter,'isHigher': isHigher, 'current_user': current_user})


# updated_by_id Data

class StockUpdate(GenericAPIView, UpdateModelMixin):
    serializer_class = RemarkstocktickSerializer
    queryset = Stocktick.objects.all()

    def patch(self, request, *args, **kwargs):
        print(request.data)
        return self.partial_update(request, *args, **kwargs)
    
    
# for filter by godown column

class Get_All_stock_List(generics.ListAPIView):
    queryset = Stocktick.objects.all()
    serializer_class = StocktickSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Godown']


# for insert data teabag view

class TeaBagView1(APIView):
    def get(self, request):
        Tea = Stocktick.objects.all()
        serializer = NewSerializer(Tea, many=True)
        return Response({'Tea': serializer.data})

    def post(self, request):
        serializer = TeaBagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
