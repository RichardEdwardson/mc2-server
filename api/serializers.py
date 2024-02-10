from rest_framework import serializers
from .models import Classroom, Chatroom, Message
from datetime import datetime

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"

class CurrentChatroomDefault:
    requires_context=True
    def __call__(self, serializer_field):
        chatroom = serializer_field.context['view'].get_object()
        return chatroom

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        extra_kwargs = {'attachment_url': {'required': False},
                        'room_id': {'default': CurrentChatroomDefault()}}

class ChatroomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, source='message_set')
    class Meta:
        model = Chatroom
        fields = "__all__"