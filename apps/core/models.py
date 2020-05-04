# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from apps import BOOLEAN_OPTIONS


class Assistants(models.Model):
    pk_assistants = models.AutoField(primary_key=True, verbose_name='Código')
    dsc_assistant = models.CharField(max_length=200, verbose_name='Description')
    flag_logon = models.SmallIntegerField(default=0, choices=BOOLEAN_OPTIONS, verbose_name='Requer Login')
    assistant_class = models.CharField(max_length=100, verbose_name='Classe do Bot')
    workspace_name = models.CharField(max_length=100, verbose_name='Workspace')
    workspace_id = models.CharField(max_length=100, verbose_name='Workspace ID')
    workspace_URL = models.TextField(verbose_name='Workspace URL')
    workspace_Key = models.CharField(max_length=100, verbose_name='Workspace Key')
    insert_date = models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Data Edição')

    class Meta:
        db_table = 'icity_assistants'
        verbose_name = 'Assistentes Virtuais'
        verbose_name_plural = 'Assistentes Virtuais'

    def __str__(self):
        return f'{self.pk_assistants}: {self.dsc_assistant}'


class Publicity(models.Model):
    pk_publicity = models.AutoField(primary_key=True, verbose_name='Código')
    fk_assistants = models.ManyToManyField(
        Assistants, blank=True, db_table='icity_pub_assistants'
    )
    title_media = models.CharField(max_length=50, verbose_name='Título')
    dsc_media = models.TextField(verbose_name='Descrição')
    file_path = models.FileField(upload_to='publicity', verbose_name='Imagens')
    insert_date = models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Data Edição')

    class Meta:
        db_table = 'icity_publicity'
        verbose_name = 'Publicidades'
        verbose_name_plural = 'Publicidades'

    def __str__(self):
        return f'{self.pk_publicity}: {self.dsc_media}'


class AssistantLastContext:
    pk_user_context = models.ForeignKey(
        User, on_delete=models.CASCADE, primary_key=True, verbose_name='Usuário'
    )
    fk_assistant = models.ForeignKey(
        Assistants, on_delete=models.CASCADE, verbose_name='Assistente'
    )
    context = models.TextField(verbose_name='Contexto')
    insert_date = models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Data Edição')

    class Meta:
        db_table = 'icity_assistants_context'
        verbose_name = 'Contextos'
        verbose_name_plural = 'Contextos'

    def __str__(self):
        return f'{self.update_date}'
