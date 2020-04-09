# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AssistantView(TemplateView):
    template_name = 'core/assistant.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AssistantLoginView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'core/assistant.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TestView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'core/test.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
