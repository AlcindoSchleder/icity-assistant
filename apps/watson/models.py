# -*- coding: utf-8 -*-
from django.db import models


class WatsonComponents(models.Model):
    pk_watson_components = models.CharField(max_length=50, primary_key=True, verbose_name='Componente')
    dsc_comp = models.CharField(max_length=100, verbose_name='Descrição')

    class Meta:
        db_table = 'watson_components'
