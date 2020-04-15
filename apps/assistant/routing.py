# -*- coding: utf-8 -*-
from django.urls import path
from .consumers import AssistantConsumer

assistant_urlpatterns = [
    path('ws/assistant/<assistant_id>/', AssistantConsumer),
    path('ws/assist_term/<assistant_id>/<terminal_id>/', AssistantConsumer),
]
