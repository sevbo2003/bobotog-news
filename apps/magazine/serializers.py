from rest_framework import serializers
from apps.magazine.models import Magazine


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = ['id', 'name', 'created_at', 'file', 'hajmi', 'downloads_count']
