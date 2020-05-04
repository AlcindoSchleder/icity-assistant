# -*- coding: utf-8 -*-
import sys
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from apps.core.models import Assistants


class AsyncMessages:

    @staticmethod
    def send_message_to_member(command: str, group: int, member: str, message: str):
        channel_layer = get_channel_layer()
        data = {
            'type': 'json.message',
            'command': command,
            'assistant_id': group,
            'terminal_id': member,
            'message': message,
        }
        member_id = f'bot_{group}_term_{member}'
        async_to_sync(channel_layer.group_send)(member_id, data)

    @staticmethod
    def send_message_to_group(command: str, group: int, message: str):
        channel_layer = get_channel_layer()
        data = {
            'type': 'json.message',
            'command': command,
            'assistant_id': group,
            'message': message,
        }
        group_id = f'bot_{group}'
        async_to_sync(channel_layer.group_send)(group_id, data)

    def process_message_from_web(
            self, command: str, group: int, member: str, message: str
    ):
        assistant = Assistants.objects.get(pk=group)
        class_bot = getattr(sys.modules[__name__], assistant.assistant_class)
        instance_bot = class_bot(group)
