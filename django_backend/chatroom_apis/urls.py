from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('create/', views.ChatRoomAPIView.as_view({
        'post': 'create',
    }), name="create_chat_room"),
    path('list/', views.ChatRoomAPIView.as_view({
        'get': 'list',
    }), name="list_user_chat_rooms"),
    path('detail/', views.ChatRoomAPIView.as_view({
        'get': 'detail',
    }), name="detail_user_chat_room"),
    path('message/', views.ChatRoomAPIView.as_view({
        'put': 'push_message',
    }), name="push_message_to_chat_room"),
]