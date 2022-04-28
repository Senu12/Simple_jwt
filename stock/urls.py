from django.urls import path,include
from . import views

urlpatterns = [
    path("showpage/<int:pk>",views.ShowPage,name='showpage'),
    # path("<int:pk>/",views.updatedata,name='updatedata'),
    path("current/<int:pk>",views.currentdata,name='currentid'),
    # path("showdata/",views.showGodown,name='show'),
]