from django.contrib.auth import authenticate, login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from account.models import UserAccountModel
from authorization.utils import get_data_for_register, get_data_for_login


class LoginPageView(View):
    template_name = 'authorization/login.html'

    def get(self, request: WSGIRequest, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request: WSGIRequest, *args, **kwargs):
        data = get_data_for_login(request.POST)

        user = authenticate(request, username=data.username, password=data.password)
        if user is not None:
            login(request, user)
            return redirect('user_profile')

        return render(request, self.template_name)


class RegisterPageView(View):
    template_name = 'authorization/register.html'

    def get(self, request: WSGIRequest, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request: WSGIRequest, *args, **kwargs):
        data = get_data_for_register(request.POST)

        if not User.objects.filter(username=data.username).exists():
            system_user = User.objects.create(
                first_name=data.first_name,
                last_name=data.last_name,
                username=data.username,
                email=data.email,
            )
            system_user.set_password(data.password)
            system_user.save()

            UserAccountModel.objects.create(user=system_user)

            user = authenticate(request, username=data.username, password=data.password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
        else:
            return render(request, self.template_name)


class LogoutPageView(View):
    def get(self, request: WSGIRequest, *args, **kwargs):
        logout(request)
        return redirect('index')
