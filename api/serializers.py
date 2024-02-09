from rest_framework import serializers
from .models import Classroom, Chatroom, Message
from datetime import datetime

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        extra_kwargs = {'created_at': {'required': False, 'default': datetime.now()},
                        'attachment_url': {'required': False}}

class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = "__all__"