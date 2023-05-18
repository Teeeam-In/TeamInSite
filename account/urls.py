from django.conf.urls.static import static
from django.urls import path

from TeamInSite import settings
from .views import UserProfileView, SaveUserProfileView, SaveUserProgLanguage, SaveUserLanguage

urlpatterns = [
    path('', UserProfileView.as_view(), name='user_profile'),
    path('save/', SaveUserProfileView.as_view(), name='save_user_profile'),
    path('save/prog_lang/', SaveUserProgLanguage.as_view(), name='save_user_prog_lang'),
    path('save/lang/', SaveUserLanguage.as_view(), name='save_user_lang'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
