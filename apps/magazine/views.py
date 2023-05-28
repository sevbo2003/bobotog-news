from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.magazine.models import Magazine
from apps.magazine.serializers import MagazineSerializer


class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    http_method_names = ['get', 'head', 'options']

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        magazine = self.get_object()
        magazine.downloads_count += 1
        magazine.save()
        return Response(status=status.HTTP_200_OK)
    