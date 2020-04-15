# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView


class AssistantView(TemplateView):
    template_name = 'core/assistant.html'

    def get(self, request, *args, **kwargs):
        params = {
            'pk':  kwargs.get('pk'),
            'dsc':  kwargs.get('dsc'),
            'message': 'Olá!',
        }
        return render(request, self.template_name, params)


