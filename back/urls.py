from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from back import settings

urlpatterns = [
    path('api/', include("api.urls")),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
