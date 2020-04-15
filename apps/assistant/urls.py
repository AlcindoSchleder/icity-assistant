from django.urls import path
from .views import AssistantView

app_name = 'assistant'
urlpatterns = [
    path('assistant/<int:pk>/<str:dsc>', AssistantView.as_view(), name='assistant'),
]
