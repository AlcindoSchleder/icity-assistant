# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Assistants, Publicity


@admin.register(Assistants)
class AssistantsAdmin(admin.ModelAdmin):
    list_display = (
        'dsc_assistant', 'pk_assistants', 'flag_logon', 'insert_date', 'update_date',
    )
    list_filter = ('dsc_assistant', 'insert_date')


@admin.register(Publicity)
class PublicityAdmin(admin.ModelAdmin):
    list_display = (
        'dsc_media', 'file_path', 'pk_publicity', 'insert_date', 'update_date',
    )
    list_filter = ('dsc_media', 'insert_date')
