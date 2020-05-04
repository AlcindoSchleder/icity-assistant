# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import WatsonComponents
from apps.core.models import Assistants, AssistantLastContext
from ibm_watson import AssistantV2
from ibm_watson import language_translator_v3
from ibm_watson import SpeechToTextV1
from ibm_watson import TextToSpeechV1
# from ibm_watson import PersonalityInsightsV3
# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_watson import ToneAnalyzerV3
# import assistant_setup
from apps import assistant as app


from ibm_cloud_sdk_core import get_authenticator_from_environment
"""
Contém o fluxo do dados do Bot
Configuração:
Configar as credenciais de todos os componentes do watson e conecta ao workspace do usuário
Operações:
1) recebe a mensagem do usuário (Web Socket)
2) mensagem é um audio? -> sim: 3 | não: 6 
3) Mensagem é áudio
4) Faz a conversão do áudio para o formato wav se for necessário (ffmpeg)
5) Faz o reconhecimento da mensagem e transforma em texto (Watson STT)
6) o Texto está na mesma linguagem do usuário? -> sim: 9 | não: 7
7) Traduz o texto recebido na linguagem de trabalho (Watson Translator)
8) armazena o lingua origina do usuário
9) Envia o texto para o Watson Assistant (Watson Assistant)
10) A mensagem está na mesma lingua da mensagem atual? -> sim: 12 | não: 11
11) Traduz a mensagem para a linguagem original do usuário (Watson Translator)
12) A mensagem original é áudio? -> sim: 13 | não
13) transforma o texto em áudio (Watson TTS)
14) converte o áudio no formato wav (ffmpeg)
15) Envia a mensagem para o Usuário (Web Socket)
"""


class PyWatsonAssistant:
    user = None
    context = None
    watson_auth = None
    watson_workspace = None
    watson_assistant = None
    watson_translator = None
    watson_tts = None
    watson_stt = None
    watson_personality_insights = None
    watson_nlu = None
    watson_tone_analyzer = None

    def process_message(
        self,
        assistant_id: int,
        terminal_id: str,
        msg_type: int,
        message,
        user: str = None
    ):
        if msg_type not in app.MESSAGE_TYPES:
            raise Exception(f'Tipo de mensagem inválido: {msg_type}')
        if assistant_id < 1:
            raise Exception(f'Código do Assistente não informado!: {message}')
        try:
            assist_obj = Assistants.objects.get(pk=assistant_id)
        except Exception as e:
            raise Exception(f'Código do Assistente não informado!: {message} - {e}')
        self.context = ''
        try:
            if user is not None or user != '':
                context_obj = AssistantLastContext.objects.get(pk=user)
                self.context = context_obj.context
        except ObjectDoesNotExist:
            context = ''
        
        if msg_type == app.TEXT_MESSAGE:
            self.watson_auth = (get_authenticator_from_environment('assistant') or
                                get_authenticator_from_environment('conversation'))
            self.watson_assistant = AssistantV2(
                version=assist_obj.version, authenticator=self.watson_auth
            );
            # self.watson_workspace = assistant_setup.init_skill(self.watson_assistant)

        user = 'magron'
        try:
            user_obj = User.objects.get(username=user)
        except ObjectDoesNotExist:
            user_obj = None
        self.user = None if user_obj is None else user_obj.username

    def config_components(self):
        if self.user is None:
            return False
        components = WatsonComponents.objects.filter(fk_user__username=self.user)
        if len(components) == 0:
            return False
        for component in components:
            # aqui pega do sdk do watson os componentes para colocar as credenciais do usuário
            pass
