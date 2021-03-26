
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Chat
from asgiref.sync import sync_to_async
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_'+str(self.room_name)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    async def disconnect(self):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await sync_to_async(Chat(room_no = self.room_name, message = message).save)()
        await self.channel_layer.group_send(self.room_group_name, {'message':message, 'type':'send_back'})
        
    async def send_back(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message':message}))
        