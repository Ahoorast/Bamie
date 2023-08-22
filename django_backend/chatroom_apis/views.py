from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from knox.auth import TokenAuthentication

from bamie.models import ChatRoom
from .serializers import ChatRoomSerializer

class ChatRoomAPIView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        # TODO: create a chatroom with owner set to request.user with empty arrays and with guidance tree id
        pass
    def list(self, request):
        # TODO: list all of the user's chatrooms
        pass
    def detail(self, request):
        # TODO: get the chatroom by pk the user must be the owner of the chatroom
        pass
    def push_message(self, request):
        # TODO: the charoom id, a message and a field which is either recieved or sent is given push the message to the corresponding array
        # if it is a recieved message this should trigger a openai api and update suggested_messages and guidance_tree_node
        pass