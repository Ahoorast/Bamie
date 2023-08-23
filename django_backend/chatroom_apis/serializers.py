from knox.serializers import UserSerializer
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from bamie.models import ChatRoom, GuidanceTree
from django.core.exceptions import ValidationError

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'
    
    def validate_guidance_tree(self, guidance_tree):
        owner = self.initial_data.get('owner')
        if guidance_tree.owner.pk != owner:
            raise ValidationError("the owner of the tree and the chatroom should be the same of the guidance tree")
        return guidance_tree
    
class ChatRoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = [
            'client',
            'guidance_tree',
        ]

    def validate_guidance_tree(self, guidance_tree):
        request = self.context.get("request")
        owner = request.user
        if guidance_tree.owner != owner:
            raise ValidationError("the owner of the tree and the chatroom should be the same of the guidance tree")
        return guidance_tree
