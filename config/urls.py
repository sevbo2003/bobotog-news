from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('api/v1/', include('apps.blog.urls')),
    path('api/v1/', include('apps.magazine.urls')),


] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
