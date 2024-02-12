import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from api.serializers import MessageSerializer
from api.models import Message, Chatroom

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        chat_history = await database_sync_to_async(self.get_chat_history)()

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        await self.send(text_data=json.dumps({"history": chat_history}))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.message_inbound = message
        await database_sync_to_async(self.save_message_to_database)()

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
    
    def get_chat_history(self):
        serializer = MessageSerializer
        queryset = Message.objects.all()
        chat_history = queryset.filter(room_id=self.room_name)
        serialized_chat_history = serializer(chat_history, many=True).data
        return serialized_chat_history
    
    def save_message_to_database(self):
        room = Chatroom.objects.all().get(room_id=self.room_name)
        Message.objects.create(room_id=room, username='test_user', content=self.message_inbound)


        


    
    