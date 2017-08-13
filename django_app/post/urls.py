from django.conf.urls import include

from django.conf.urls import url
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from post import views

from django.conf.urls import url, include

from post.views import PostViewSet, UserViewSet, api_root

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
# API endpoints
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^snippets/$',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     url(r'^users/$',
#         views.UserList.as_view(),
#         name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])
#
# # 탐색 가능한 API를 위한 로그인/로그아웃 뷰
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)

# 이제 API URL을 라우터가 자동으로 인식합니다
# 추가로 탐색 가능한 API를 구현하기 위해 로그인에 사용할 URL은 직접 설정을 했습니다
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]