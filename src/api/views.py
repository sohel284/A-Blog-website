from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions


from blog.models import Blog,User
from api.serializers import BlogSerializer, UserSerializer


class BlogListCreateAPIView(ListCreateAPIView):
    permission_class = permissions.AllowAny()
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()




class UserListCreateAPIView(ListCreateAPIView):
    permission_class = permissions.AllowAny()
    serializer_class = UserSerializer
    queryset = User.objects.all()







