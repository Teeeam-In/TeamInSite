from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from account.models import UserAccountModel, LanguagesModel, HardSkillsModel


class UserProfileView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'account/user_profile.html'

    def get(self, request: WSGIRequest, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                'user': UserAccountModel.objects.get(user=request.user),
                'title': 'User Profile'
            }
        )

    def post(self, request: WSGIRequest, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                'user': UserAccountModel.objects.get(user=request.user),
                'title': 'User Profile'
            }
        )


class SaveUserProfileView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request: WSGIRequest, *args, **kwargs):
        user_profile = UserAccountModel.objects.filter(user=request.user)
        system_user = User.objects.filter(username=request.user)

        data: dict = eval(request.POST['data'])

        user_profile.update(
            phone=data['phone'],
            address=data['address'],
            occupation=data['occupation'],
            description=data['description'],
            telegram=data['telegram'],
            discord=data['discord'],
            github=data['github'],
            portfolio=data['portfolio'],
        )
        system_user.update(email=data['email'])

        return JsonResponse(request.POST, safe=False)


class SaveUserProgLanguage(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request: WSGIRequest, *args, **kwargs):
        hard_skill = HardSkillsModel.objects.create(
            programming_language=request.POST['progLanguage'],
            description=request.POST['progLanguageDescription']
        )
        user_profile = UserAccountModel.objects.get(user=request.user)
        user_profile.hard_skills.add(hard_skill)

        return JsonResponse(request.POST, safe=False)


class SaveUserLanguage(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request: WSGIRequest, *args, **kwargs):
        language = LanguagesModel.objects.create(
            language=request.POST['language'],
            language_level=request.POST['languageDescription']
        )
        user_profile = UserAccountModel.objects.get(user=request.user)
        user_profile.languages.add(language)

        return JsonResponse(request.POST, safe=False)
