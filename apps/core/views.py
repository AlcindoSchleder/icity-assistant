# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Assistants


class HomeView(TemplateView):
    template_name = 'core/index.html'
    pk_assistant = 0

    def get(self, request, *args, **kwargs):
        qry_assist = Assistants.objects.all()
        return render(request, self.template_name, {'qra': qry_assist})

    def post(self, request, *args, **kwargs):
        assistant = None
        msg = ''
        self.pk_assistant = kwargs.get('pk_assistant')
        if self.pk_assistant is not None:
            try:
                assistant = Assistants.objects.get(pk=self.pk_assistant)
            except ObjectDoesNotExist:
                msg = f'Assistente {self.pk_assistant} não foi encontrado!!'
                assistant = None
            if assistant is not None:
                return redirect(
                    f'core:land_page', pk_assistant=assistant.pk_assistants
                )
        else:
            msg = f'Assistente é nulo!!'
        assistant = Assistants.objects.all()
        return render(request, self.template_name, {'qra': assistant, 'message': msg})


class LandPageView(TemplateView):
    template_name = ''

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk_assistant')
        msg = ''
        assistant = None
        try:
            assistant = Assistants.objects.get(pk=pk)
        except ObjectDoesNotExist:
            msg = f'Assistente {self.pk_assistant} não foi encontrado!!'
        if assistant is None:
            return redirect('core:index', {'message': msg})
        self.template_name = f'core/{assistant.workspace_name}.html'
        params = {
            'bot': assistant.dsc_assistant,
            'pk': assistant.pk_assistants,
        }
        return render(request, self.template_name, params)


class AssistantView(TemplateView):
    template_name = 'core/assistant.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TestView(TemplateView):
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    template_name = 'core/test.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
