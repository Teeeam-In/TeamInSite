from django.conf.urls.static import static
from django.urls import path

from TeamInSite import settings
from .views import RegisterPageView, LoginPageView, LogoutPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
