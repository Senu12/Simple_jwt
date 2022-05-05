from django.urls import path,include
from .views import *

urlpatterns = [
    path('List/',StockticklistView.as_view()),
    path('update/<int:pk>',StocktickView.as_view()),
    # path('update/<int:pk>',Stockupdate.as_view()),
]
