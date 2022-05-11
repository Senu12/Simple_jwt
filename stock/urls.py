from django.urls import path,include
# from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("showpage/<int:pk>",views.ShowPage,name='showpage'),
    # path("status/",views.updatedata,name='status'),
    path('api/', views.Get_All_stock_List.as_view()),
    path("Listofdata/",views.DropDown.as_view(),name='Alldata'),
    path('api/<int:pk>', views.Get_stock_List.as_view()),
    path("api/<int:pk>/update/", views.StockUpdate.as_view(), name='update'),
    # path("cases/", views.StockUpdate.as_view(), name='cases'),
    # path('duplicate/',views.duplicatevalue),
    path('signup/', views.UserRegister.as_view()),#
    path('signin/', views.LoginView.as_view()),
    path('logout/',views.Logout.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # path("login/",views.Loginpage),
    # path('login/', LoginView.as_view(), name='login'),
    path('higher/',views.higher),
    # path('lower/',views.lower),
    # path('remarks/<int:pk>',views.RemarksView.as_view()),
]