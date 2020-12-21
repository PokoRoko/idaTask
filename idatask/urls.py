from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('saveimage.urls')),
]

# Определяем работу папки медиа в режиме дебага, для отображения изображений
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

