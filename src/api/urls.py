from django.urls import path

from api.views import BlogListCreateAPIView
from api.views import UserListCreateAPIView

urlpatterns = [
    path('', BlogListCreateAPIView.as_view(), name='blog_create'),
   
    path('user/', UserListCreateAPIView.as_view(), name='user-list'),
]
