from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BookForm
from Table.models import Stocktick
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from Table.serializers import StocktickSerializer, UpdateStocktickSerializer
from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Count
# from django.db.models import Avg, Count, Min, Sum
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend

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


# just for practice
class DropDown(APIView):

    def get(self, request, format=None):
        # duplicates = Stocktick.objects.values(
        #     'OurLot').annotate(ourlot_count=Count('OurLot'))
        # print(duplicates)
        # queryset = Stocktick.objects.all()
        # serializer = StocktickSerializer(queryset,many=True)
        # return Response(serializer.data)
        if self.request.method == "GET" and 'selected_Godown' in request.GET:
            gData = Stocktick.objects.values(
                'Godown').distinct().exclude(Godown='B')
            # print(gData)
            Godown_filter = request.GET.get('selected_Godown')
            # print(Godown_filter)
            all_data = Stocktick.objects.filter(Godown=Godown_filter)

            total_case = Stocktick.objects.filter(
                Godown=Godown_filter).aggregate(Sum('Cases')).get('Cases__sum')
            print(total_case)

            total_p_case = Stocktick.objects.filter(
                Godown=Godown_filter).aggregate(Sum('Pcase'))
            p = total_p_case['Pcase__sum']

        else:
            gData = Stocktick.objects.values(
                'Godown').distinct().exclude(Godown='B')
            print(gData)
            print(gData[0])
            all_data = Stocktick.objects.filter(Godown=gData[0]['Godown'])
            total_case = Stocktick.objects.filter(
                Godown=gData[0]['Godown']).aggregate(Sum('Cases')).get('Cases__sum')
            print(total_case)
            total_p_case = Stocktick.objects.filter(
                Godown=gData[0]['Godown']).aggregate(Sum('Pcase'))
            p = total_p_case['Pcase__sum']
            Godown_filter = gData[0]['Godown']

        return render(request, 'stock/table.html', {'key1': all_data, 'key2': gData, 'sum': total_case, 'case': p, 'selected': Godown_filter})


# for upate data
class StockUpdate(generics.UpdateAPIView):
    queryset = Stocktick.objects.all()
    serializer_class = StocktickSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


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
