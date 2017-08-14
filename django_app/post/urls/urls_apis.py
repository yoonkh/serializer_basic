
from django.conf.urls import url
from rest_framework.authtoken import views

from post.apis import PostListAPIView, PostCreateAPIView, PostUpdateDestroyAPIView
from .. import apis

urlpatterns = [
    url(r'^list/$', PostListAPIView.as_view()),
    url(r'^create/$', PostCreateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', PostUpdateDestroyAPIView.as_view()),
]