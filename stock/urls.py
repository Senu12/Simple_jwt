from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', views.Get_All_stock_List.as_view()),
    path("Listofdata/", views.DropDown.as_view(), name='Alldata'),
    path('api/<int:pk>', views.Get_stock_List.as_view()),
    path("api/<int:pk>/update/", views.StockUpdate.as_view(), name='update'),
    path('api-auth/', include('rest_framework.urls')),
    path('Tea/', views.TeaBagView1.as_view()),
]
