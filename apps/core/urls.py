# -*- coding: utf-8 -*-
from django.urls import path
from .views import HomeView, TestView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('tests/', TestView.as_view(), name='test'),
]
