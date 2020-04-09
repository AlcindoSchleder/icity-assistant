# -*- coding: utf-8 -*-
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class DisplayConsumer(AsyncWebsocketConsumer):
    display_id = ''
    user_id = ''
    group_id = ''

    async def connect(self):
        self.display_id = self.scope['url_route']['kwargs'].get('display_id')
        self.user_id = self.scope['url_route']['kwargs'].get('user_id')
        self.group_id = f'user_{self.user_id}_display_{self.display_id}' \
            if self.display_id is not None else f'user_{self.user_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.group_id,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_id,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        command = text_data_json.get('command')
        user_id = text_data_json.get('user_id')
        display_id = text_data_json.get('display_id')
        message = text_data_json.get('message')

        # group = self.channel_name if display_id is not None else self.group_id
        # Send message to display if display_id = none send to group 'user_id'
        print(f'F[receive] Enviando a mensagem para: {self.group_id}')
        await self.channel_layer.group_send(
            self.group_id,
            {
                'type': 'json.message',
                'command': command,
                'user_id': user_id,
                'display_id': display_id,
                'message': message,
            }
        )
        print('F[receive] Fim do recebimento da mensagem.....')

    # Receive message from room group
    async def json_message(self, event):
        command = event['command']
        user_id = event['user_id']
        display_id = event['display_id']
        message = event['message']

        print(f'F[json_message]: sending message "{message}" to {user_id}/{display_id} with command {command}')
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'command': command,
            'user_id': user_id,
            'display_id': display_id,
            'message': message,
        }))
