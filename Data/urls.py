from django.contrib import admin
from django.urls import URLPattern, path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('create', PostBlog, basename='post_data')
# router.register('update', UpdateBlog,basename='update')
router.register("Blog", BlogModelViewSet, basename='Blog')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', UserRegister.as_view()),#
    path('signin/', LoginView.as_view()),#
    # path('create/',PostBlog.as_view()),
    # path('List/', ListBlogs.as_view(),name='data'),
    # path('update/<int:pk>',UpdateBlog.as_view()),
    # path('delete/<int:pk>',DestroyBlog.as_view()),
    path('logout/',Logout.as_view()),#
]
