from django.conf.urls.static import static
from django.urls import path

from TeamInSite import settings
from index.views import AboutView

urlpatterns = [
    path('', AboutView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
