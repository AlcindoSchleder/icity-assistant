# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Assistants


@admin.register(Assistants)
class AssistantsAdmin(admin.ModelAdmin):
    list_display = (
        'dsc_assistant', 'pk_assistants', 'flag_require_user', 'insert_date', 'update_date',
    )
    list_filter = ('dsc_assistant', 'insert_date')
