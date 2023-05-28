from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.magazine.views import MagazineViewSet


router = DefaultRouter()

router.register('magazines', MagazineViewSet, basename='magazines')


urlpatterns = [
    path('', include(router.urls)),
]
