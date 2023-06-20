from rest_framework import serializers
from apps.blog.models import Category, Post, PostImage
from django.conf import settings

DOMAIN = "https://uzunpro.uz"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
    

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image', 'video']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['image']:
            if data['image'][0] == 'h':
                return data
            data['image'] = DOMAIN + data['image']
        return data


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    postimage_set = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'category','author', 'created_at', 'updated_at', 'dolzarb', 'is_featured', 'slug',
                  'views', 'postimage_set']
    

class PostRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    postimage_set = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'content', 'created_at', 'updated_at', 'dolzarb', 'is_featured', 'slug',
                  'views', 'postimage_set']
