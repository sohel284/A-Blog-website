from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='blog_create'),
    path('details/(?P<slug>[\w\-]+)/$', views.blog_details, name='blog_detail'),
    path('likes/<pk>/', views.liked, name='liked_post'),
    path('unlikes/<pk>/', views.unliked, name='unliked_post'),
    path('my-blog/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),

]