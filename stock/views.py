from django.shortcuts import render
from Table.models import Stocktick
# from Table.serializers import StocktickSerializer,UpdateStocktickSerializer

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


# def updatedata(request, id):
#     if request.method == 'POST':
#         data = Stocktick.objects.get(pk=id)
#         new_data = StocktickSerializer(request.POST, instance=data)
#         if new_data.is_valid():
#             new_data.save()
#     else:
#         data = Stocktick.objects.get(pk=id)
#         new_data = StocktickSerializer(instance=data)
#     return render(request, 'stock/update.html', {'data': new_data})

# for current data


def currentdata(request, pk):
    gData = Stocktick.objects.values('godown').distinct()
    all_data = Stocktick.objects.filter(godown=pk)
    return render(request, 'stock/table.html', {'key1': all_data, 'key2': gData})
