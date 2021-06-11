from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('app_pages.urls')),
    path('blog/', include('app_blog.urls', namespace='blog')),
    path('portfolio/', include('app_portfolio.urls')),
    path('stats/', include('app_stats.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


