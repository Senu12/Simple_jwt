from django.urls import path,include
from . import views

urlpatterns = [
    path("showpage/<int:pk>",views.ShowPage,name='showpage'),
    # path("status/",views.updatedata,name='status'),
    path('api/', views.Get_All_stock_List.as_view()),
    path("Listofdata/",views.DropDown.as_view(),name='Alldata'),
    path('api/<int:pk>', views.Get_stock_List.as_view()),
    path("api/<int:pk>/update/", views.StockUpdate.as_view(), name='update'),
    path("cases/", views.StockUpdate.as_view(), name='cases'),
    # path('duplicate/',views.duplicatevalue),
]