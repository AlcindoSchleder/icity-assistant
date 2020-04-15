# -*- coding: utf-8 -*-
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class AssistantConsumer(AsyncWebsocketConsumer):
    assistant_id = ''
    terminal_id = ''
    group_id = ''

    async def connect(self):
        self.assistant_id = self.scope['url_route']['kwargs'].get('assistant_id')
        self.terminal_id = self.scope['url_route']['kwargs'].get('terminal_id')
        self.group_id = f'display_{self.assistant_id}_user_{self.terminal_id}' \
            if self.terminal_id is not None else f'display_{self.assistant_id}'

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
        assistant_id = text_data_json.get('assistant_id')
        terminal_id = text_data_json.get('terminal_id')
        message = text_data_json.get('message')

        # group = self.channel_name if assistant_id is not None else self.group_id
        # Send message to display if assistant_id = none send to group 'terminal_id'
        print(f'F[receive] Enviando a mensagem para: {self.group_id}')
        await self.channel_layer.group_send(
            self.group_id,
            {
                'type': 'json.message',
                'command': command,
                'assistant_id': assistant_id,
                'terminal_id': terminal_id,
                'message': message,
            }
        )
        print('F[receive] Fim do recebimento da mensagem.....')

    # Receive message from room group
    async def json_message(self, event):
        command = event['command']
        assistant_id = event['assistant_id']
        terminal_id = event['terminal_id']
        message = event['message']

        print(f'F[json_message]: sending message "{message}" to {assistant_id}/{terminal_id} with command {command}')
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'command': command,
            'assistant_id': assistant_id,
            'terminal_id': terminal_id,
            'message': message,
        }))
