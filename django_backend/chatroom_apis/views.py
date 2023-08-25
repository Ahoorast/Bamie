from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from knox.auth import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone


from bamie.models import ChatRoom, GuidanceTree
from .serializers import ChatRoomSerializer, ChatRoomCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.shortcuts import get_object_or_404
from .prompt import OpenaiResponse

class NoPagination(PageNumberPagination):
    page_size = None

class ChatRoomAPIViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ChatRoom.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        recieved_messages=[],
                        suggested_messages=[],
                        sent_messages=[],
                        recieved_messages_timestamp=[],
                        sent_messages_timestamp=[],
                        guidance_tree_node=0,
                        )
        
    def create_empty_tree_for_user(self):
        guidance_tree = GuidanceTree.objects.create(
            owner=self.request.user,
            position_array_x_axis=[0],
            position_array_y_axis=[0],
            parent_array=[-1],
            example_input_array=[" "],
            example_output_array=["Hello, How can I help you today"], 
        )
        guidance_tree.save()

    def create_playground_chatroom(self, request):
        user_guidance_trees = GuidanceTree.objects.filter(owner=request.user)
        if user_guidance_trees.count() == 0:
            self.create_empty_tree_for_user()
            user_guidance_trees = GuidanceTree.objects.filter(owner=request.user)
        chatroom = ChatRoom.objects.create(
            owner=self.request.user,
            client="Playground",
            recieved_messages=[],
            suggested_messages=[],
            sent_messages=[user_guidance_trees[0].example_output_array[0]],
            recieved_messages_timestamp=[],
            sent_messages_timestamp=[timezone.now()],
            guidance_tree_node=0,
            guidance_tree=user_guidance_trees[0]
        )
        chatroom.save()
        serialized_chatroom = ChatRoomSerializer(chatroom)
        return Response(serialized_chatroom.data, status=200)
    
    def create(self, request):
        serializer = ChatRoomCreateSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        user = request.user
        chatroom = get_object_or_404(self.queryset.filter(owner=user), pk=pk)
        serialized_chatroom = ChatRoomSerializer(chatroom)
        return Response(serialized_chatroom.data, status=200)
    
    def list(self, request):
        user = request.user
        # TODO: order by last message timestamp
        list_view = ListAPIView.as_view(queryset=self.queryset.filter(owner=user), 
                                        serializer_class=ChatRoomSerializer, 
                                        pagination_class=NoPagination,
                                        )
        return list_view(request._request).render()
    
    def push_message(self, request):
        """
            {
                "chatroom_id": 1,
                message: "filan",
                "type": "given/recieved",
            }
        """
        try:
            chatroom_id = self.request.data.get('chatroom_id')
            message = self.request.data.get('message')
            type = self.request.data.get('type')
        except KeyError:
            return Response(status=400)
        user = request.user
        chatroom = get_object_or_404(self.queryset.filter(owner=user), pk=chatroom_id)
        is_recieved = type == 'recieved'
        if is_recieved:
            chatroom.recieved_messages.append(message)
            chatroom.recieved_messages_timestamp.append(timezone.now())
            openai_response = OpenaiResponse(chatroom.last_messages(), chatroom.guidance_tree.children_templates(chatroom.guidance_tree_node))
            suggested_message = openai_response['response']
            guidance_tree_node = chatroom.guidance_tree.nthChildIndex(chatroom.guidance_tree_node, openai_response['id'])
            chatroom.suggested_messages.append(suggested_message)
            chatroom.guidance_tree_node = guidance_tree_node
        else:
            chatroom.sent_messages.append(message)
            chatroom.sent_messages_timestamp.append(timezone.now())
        chatroom.save()
        serialized_chatroom = ChatRoomSerializer(chatroom)
        return Response(serialized_chatroom.data, status=200)