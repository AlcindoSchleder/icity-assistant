from django.db import models
from apps import BOOLEAN_OPTIONS


class Assistants(models.Model):
    pk_assistants = models.AutoField(primary_key=True, verbose_name='Código')
    dsc_assistant = models.CharField(max_length=200, verbose_name='Description')
    flag_require_user = models.SmallIntegerField(default=0, choices=BOOLEAN_OPTIONS, verbose_name='Requer Login')
    insert_date = models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Data Edição')

    class Meta:
        db_table = 'icity_assistants'
        verbose_name = 'Assistentes Virtuais'
        verbose_name_plural = 'Assistentes Virtuais'

    def __str__(self):
        return f'{self.pk_assistants}: {self.dsc_assistant}'
