from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.blog.models import Category, Post
from apps.blog.serializers import CategorySerializer, PostSerializer, PostImageSerializer


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
    