# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class WatsonComponents(models.Model):
    TYPES_COMPONENT = (
        ('Workspace Assistant', 'Seu bot na IBM Cloud'),
        ('Watson Assistant', 'Assistente Virtual Watson'),
        ('Watson Studio', 'Aprendizado de Máquina Embarcado'),
        ('Watson Machine Learning', 'Aprendizado de Máquina'),
        ('Compare and Comply', 'Processamento de Documentos'),
        ('Discovery', 'Busca Analítica de Conteúdo'),
        ('Knowledge Catalog', 'Busca, Cataloga e Compartilha Documentos'),
        ('Knowledge Studio', 'Aprendizado de Linguagem de Domínio'),
        ('Language Translator', 'Tradutor de Linguagens'),
        ('Natural Language Understanding', 'Analisador de Textos'),
        ('Personality Insights', 'Gerar Perfil Psicológico'),
        ('SpeechToText', 'Reconheciento de Fala'),
        ('TextToSpeech', 'Transforma Texto em Fala'),
        ('Visual Recognition', 'Reconhecimento de Imagens'),
    )
    pk_watson_components = models.CharField(max_length=50, primary_key=True, verbose_name='Nome do Componente')
    component_type = models.CharField(max_length=50, choices=TYPES_COMPONENT, verbose_name='Tipo')
    dsc_comp = models.CharField(max_length=100, verbose_name='Descrição')
    insert_date = models.DateTimeField(auto_now_add=True, default=datetime.now(), verbose_name='Data Inserção')
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Data Inserção')

    class Meta:
        db_table = 'watson_components'
        verbose_name = 'Componentes IBM Watson'
        verbose_name_plural = 'Componentes IBM Watson'


class WatsonAccess(models.Model):
    pk_watson_access = models.AutoField(primary_key=True, verbise_name='Código')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Proprietário')
    fk_watson_components = models.ForeignKey(WatsonComponents, on_delete=models.CASCADE, verbose_name='Componente')
    api_key = models.CharField(max_length=180, null=True, blank=True, verbose_name='API Key')
    user_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Usuário')
    password = models.CharField(max_length=150, null=True, blank=True, verbose_name='Senha')
    insert_date = models.DateTimeField(auto_now_add=True, default=datetime.now(), verbose_name='Data Inserção')
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Data Inserção')

    class Meta:
        db_table = 'watson_access'
        verbose_name = 'Chaves Accesso Componentes'
        verbose_name_plural = 'Chaves Accesso Componentes'
        indexes = [
           models.Index(fields=['fk_user', 'fk_watson_components']),
        ]


class WatsonLogs(models.Model):
    pk_watson_logs = models.AutoField(primary_key=True, verbose_name='Código')
    fk_watson_components = models.ForeignKey(WatsonComponents, on_delete=models.CASCADE, verbose_name='Componente')
    fk_user = models.ForeignKey(User, null=True, blak=True, on_delete=models.CASCADE, verbose_name='Usuário')
    sender_name = models.CharField(max_length=100, null=True, blak=True, verbose_name='Nome do Usuário')
    sender_message = models.TextField(verbose_name='Mensagem Enviada')
    response_message = models.TextField(verbose_name='Resposta da Mensagem')
    flag_invalid_response = models.SmallIntegerField(default=0, verbose_name='Resposta Inválida')
    flag_resolve = models.SmallIntegerField(default=0, verbose_name='Resolvida')
    insert_date = models.DateTimeField(auto_now_add=True, default=datetime.now(), verbose_name='Data Inserção')
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Data Inserção')

    class Meta:
        db_table = 'watson_logs'
        verbose_name = 'Log de Mensagens'
        verbose_name_plural = 'Log de Mensagens'
        indexes = [
           models.Index(fields=['fk_user', 'fk_watson_components', 'flag_invalid_response']),
        ]
