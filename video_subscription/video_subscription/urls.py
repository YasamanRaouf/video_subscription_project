# video_subscription/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('videos.urls')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)