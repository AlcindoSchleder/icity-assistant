# -*- coding: utf-8 -*-
from django.urls import path
from .views import HomeView, LandPageView, AssistantView, TestView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('<int:pk_assistant>', HomeView.as_view(), name='index'),
    path('bot/<int:pk>/<str:dsc>', LandPageView.as_view(), name='land_page'),
    path('bot_assistant/<int:pk>/<str:dsc>', AssistantView.as_view(), name='assistant'),
    path('tests/', TestView.as_view(), name='test'),
]
