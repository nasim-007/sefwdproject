
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('album/', include('album.urls', namespace='album')),
    path('', include('nimuit.urls', namespace='nimuit')),
    path('bootstrap/', include('bootstrap.urls', namespace='bootstrap')),
    path('carousel/', include('carousel.urls', namespace='carousel')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)