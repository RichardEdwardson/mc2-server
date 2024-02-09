from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Classroom, Chatroom, Message
from .serializers import ClassroomSerializer, ChatroomSerializer, MessageSerializer

# Create your views here.
class ClassroomView(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filterset_fields = ['name']

class ChatroomView(viewsets.ModelViewSet):
    queryset = Chatroom.objects.all()
    serializer_class = ChatroomSerializer

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        chatroom = self.get_object()
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        


    # def get_queryset(self):
    #     if self.request.method == 'GET':
    #         return Chatroom.objects.all()
    #     else:
    #         return Message.objects.all()
    
    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return ChatroomSerializer
    #     else:
    #         return MessageSerializer
