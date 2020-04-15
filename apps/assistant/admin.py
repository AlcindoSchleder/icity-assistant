# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import WatsonComponents, WatsonAccess, WatsonLogs


@admin.register(WatsonComponents)
class AssistantComponentsAdmin(admin.ModelAdmin):
    list_display = (
        'pk_watson_components', 'dsc_comp', 'insert_date', 'update_date',
    )
    list_filter = ('dsc_comp', 'insert_date')

    # fieldsets = (
    #     (None, {
    #         'fields': ('pk_watson_components',)
    #     }),
    #     ('Components', {
    #         'fields': ('dsc_comp',)
    #     }),
    # )


@admin.register(WatsonAccess)
class AssistantAccessAdmin(admin.ModelAdmin):
    list_display = (
        'fk_watson_components', 'component_name', 'component_url', 'insert_date', 'update_date',
    )


@admin.register(WatsonLogs)
class AssistantLogsAdmin(admin.ModelAdmin):
    list_display = (
        'fk_user', 'fk_watson_components', 'sender_name', 'sender_message',
        'flag_invalid_response', 'flag_resolve', 'insert_date', 'update_date',
    )
