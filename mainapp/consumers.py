
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_'+str(self.room_name)
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_layer)
        self.accept()
    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_layer)
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {'message':message, 'type':'send_back'})
        
    def send_back(self, event):
        message = event['message']
        self.send(text_data=json.dumps({'message':message}))
        