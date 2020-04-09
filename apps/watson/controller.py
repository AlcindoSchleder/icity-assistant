# -*- coding: utf-8 -*-
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class AsyncMessages:

    @staticmethod
    def send_message_to_member(command: str, group: int, member: str, message: str):
        channel_layer = get_channel_layer()
        data = {
            'type': 'json.message',
            'command': command,
            'display_id': group,
            'user_id': member,
            'message': message,
        }
        member_id = f'display_{group}_user_{member}'
        async_to_sync(channel_layer.group_send)(member_id, data)

    @staticmethod
    def send_message_to_group(command: str, group: int, message: str):
        channel_layer = get_channel_layer()
        data = {
            'type': 'json.message',
            'command': command,
            'display_id': group,
            'message': message,
        }
        group_id = f'user_{group}'
        async_to_sync(channel_layer.group_send)(group_id, data)
