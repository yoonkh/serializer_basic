from rest_framework import generics
from rest_framework.permissions import AllowAny

from post.models import Post
from post.serializers import PostSerializer, PostCreateSerializer


class PostListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer


class PostUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()

