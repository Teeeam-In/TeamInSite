from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import View


class AboutView(View):
    template_name = 'index.html'

    def get(self, request: WSGIRequest, *args, **kwargs):
        return render(request, self.template_name, {'user': request.user})
