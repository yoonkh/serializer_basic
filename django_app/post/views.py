from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, mixins, generics, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import permissions
from post.models import Post
from post.permissions import IsOwnerOrReadOnly
from post.serializers import UserSerializer, PostSerializer


# class JSONResponse(HttpResponse):
#     """
#     콘텐츠를 JSON으로 변환한 후 HttpResponse 형태로 반환합니다.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# def snippet_list(request):
#     """
#     코드 조각을 모두 보여주거나 새코드 조각을 만듭니다.
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         snippet = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)


# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetList(APIView):
#     """
#     코드 조각을 모두 보여주거나 새코드 조각을 만급니다.
#     """
#     def get(self, request, format=None):
#         snippet = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet, many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     코드 조각 조회, 업데이트, 삭제
#     :param request:
#     :param pk:
#     :return:
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     코드 조각 조회, 업데이트, 삭제
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    이 뷰셋은 `list`와 `detail` 기능을 자동으로 지원합니다
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

class PostViewSet(viewsets.ModelViewSet):
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원합니다

	여기에 `highlight` 기능의 코드만 추가로 작성했습니다
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        return Response("ok")

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.highlighted)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

