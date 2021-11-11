
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as mediaserve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('album/', include('album.urls', namespace='album')),
    path('', include('nimuit.urls', namespace='nimuit')),
    path('bootstrap/', include('bootstrap.urls', namespace='bootstrap')),
    path('carousel/', include('carousel.urls', namespace='carousel')),

    
]


urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                     mediaserve, {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)