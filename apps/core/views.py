# -*- coding: utf-8 -*-
import re
from unicodedata import normalize
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.models import Q
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Assistants, Publicity


class HomeView(TemplateView):
    template_name = 'core/index.html'
    pk_assistant = 0

    def get(self, request, *args, **kwargs):
        msg = ''
        try:
            qry_assist = Assistants.objects.all()
            publicity = Publicity.objects.filter(fk_assistants=None).order_by('pk_publicity')
        except Exception as e:
            msg = f'Erro ao carregar o banco de dados!! - ({e})'
        params = {
            'qra': qry_assist,
            'message': msg,
            'publicity': publicity,
        }
        return render(request, self.template_name, params)

    @staticmethod
    def slugify(s: str):
        s = normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')
        s = re.sub("[^a-zA-Z]+", '_', s)
        return re.sub("(^_)|(_$)", '', s).lower()

    def post(self, request, *args, **kwargs):
        assistant = None
        msg = ''
        self.pk_assistant = kwargs.get('pk_assistant')
        if self.pk_assistant is not None:
            try:
                assistant = Assistants.objects.get(pk=self.pk_assistant)
                publicity = Publicity.objects.filter(fk_assistants=None).order_by('pk_publicity')
            except ObjectDoesNotExist:
                msg = f'Assistente {self.pk_assistant} não foi encontrado!!'
                assistant = None
            if assistant is not None:
                name = self.slugify(assistant.dsc_assistant)
                return redirect(
                    f'core:land_page',
                    pk=assistant.pk_assistants,
                    dsc=name,
                )
        else:
            msg = f'Assistente é nulo!!'
        assistant = Assistants.objects.all()
        params = {
            'qra': assistant,
            'message': msg,
            'publicity': publicity,
        }
        return render(request, self.template_name, params)


class LandPageView(TemplateView):
    template_name = ''

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        msg = ''
        assistant = None
        try:
            assistant = Assistants.objects.get(pk=pk)
            publicity = Publicity.objects.filter(
                Q(fk_assistants=None) | Q(fk_assistants=pk)
            ).order_by('pk_publicity')
        except ObjectDoesNotExist:
            msg = f'Assistente {self.pk_assistant} não foi encontrado!!'
        if assistant is None:
            return redirect('core:index', {'message': msg})
        self.template_name = f'core/{assistant.workspace_name}.html'
        params = {
            'bot': assistant.dsc_assistant,
            'pk': assistant.pk_assistants,
            'publicity': publicity,
        }
        return render(request, self.template_name, params)


class TestView(TemplateView):
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    template_name = 'core/test.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
