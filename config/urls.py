from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Bobotog' news API",
        default_version='v1.0.0',
        description="Bobotog' news API",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.blog.urls')),
    path('api/v1/', include('apps.magazine.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
