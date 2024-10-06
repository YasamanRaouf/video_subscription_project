from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videos.urls')),  # وارد کردن مسیرهای اپلیکیشن videos
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]

# مسیر فایل‌های استاتیک
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
