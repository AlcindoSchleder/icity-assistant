# -*- coding: utf-8 -*-
from django.urls import path
from .consumers import DisplayConsumer

watson_urlpatterns = [
    path('ws/user/<user_id>/', DisplayConsumer),
    path('ws/display/<user_id>/<display_id>/', DisplayConsumer),
]
