from rest_framework import generics
from rest_framework.permissions import AllowAny

from post.serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
