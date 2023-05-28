from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.blog.models import Category, Post
from apps.blog.serializers import CategorySerializer, PostSerializer, PostRetrieveSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'head', 'options']

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        category = self.get_object()
        pagination = self.paginate_queryset(category.post_set.all())
        if pagination is not None:
            serializer = PostSerializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(category.post_set.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'head', 'options']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostRetrieveSerializer
        return super().get_serializer_class()
    
    def retrieve(self, request, *args, **kwargs):
        saved_views = request.session.get('views', [])
        post = self.get_object()
        if post.id not in saved_views:
            post.views += 1
            post.save()
            saved_views.append(post.id)
            request.session['views'] = saved_views
        return super().retrieve(request, *args, **kwargs)
    
    @action(detail=True, methods=['get'])
    def related_posts(self, request, pk=None):
        post = self.get_object()
        pagination = self.paginate_queryset(post.category.post_set.all().exclude(id=post.id))
        if pagination is not None:
            serializer = PostSerializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(post.category.post_set.all().exclude(id=post.id), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def featured_posts(self, request):
        pagination = self.paginate_queryset(Post.objects.filter(is_featured=True))
        if pagination is not None:
            serializer = PostSerializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(Post.objects.filter(is_featured=True), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def dolzarb_posts(self, request):
        pagination = self.paginate_queryset(Post.objects.filter(dolzarb=True))
        if pagination is not None:
            serializer = PostSerializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(Post.objects.filter(dolzarb=True), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    