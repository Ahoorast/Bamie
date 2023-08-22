from knox.serializers import UserSerializer
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from bamie.models import ChatRoom

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'