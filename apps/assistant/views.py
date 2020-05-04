# -*- coding: utf-8 -*-
import uuid
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Assistants


class AssistantView(TemplateView):
    template_name = 'core/assistant.html'
    bot_context = None
    pk_assistant = None
    assist_obj = None

    def get(self, request, *args, **kwargs):
        user = '';
        msg = 'Olá!'
        try:
            self.pk_assistant = kwargs.get('pk')
            if self.pk_assistant is None:
                raise Exception('Parâmetro "Código do Assistente" não foi passado na url!')
            self.assist_obj = Assistants.objects.get(pk=self.pk_assistant)
        except Exception as e:
            msg = f'Error ao ler a tabela de Assistentes! {e}'
            return redirect('home:index', pk=self.pk_assistant, message=msg)

        # Store the unique id for this terminal
        if request.session.get('terminal_id') is None:
            request.session['terminal_id'] = uuid.uuid4()
        # Check if this assistant require login and if user already logged in
        if bool(self.assist_obj.flag_logon) and not request.user.is_authenticated:
            return redirect('login:login', dsc_assistant=kwargs.get('dsc'))
        else:
            user = request.user.username
        # send params to template view
        params = {
            'user': user,
            'pk':  self.pk_assistant,
            'dsc':  kwargs.get('dsc'),
            'message': msg,
            'terminal_id': request.session.get('terminal_id'),
        }
        return render(request, self.template_name, params)

    def post(self, request, *args, **kwargs):
        self.bot_context = kwargs.get('bot_context')
        url = kwargs.get('redirect_url')
        if self.bot_context is not None:
            request.session['bot_context'] = self.bot_context
        request.user.logout()
        return redirect(url)
