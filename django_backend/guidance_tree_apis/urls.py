from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.GuidanceTreeAPIViewSet.as_view({
        'post': 'create',
    }), name="create_guidance_tree"),
    path('list/', views.GuidanceTreeAPIViewSet.as_view({
        'get': 'list',
    }), name="list_guidance_tree"),
    path('retrieve/<int:pk>/', views.GuidanceTreeAPIViewSet.as_view({
        'get': 'retrieve',
    }), name="detail_guidance_tree"),
    path('retrieve/', views.GuidanceTreeAPIViewSet.as_view({
        'get': 'retrieve',
    }), name="detail_guidance_tree"),
    path('update/<int:pk>/', views.GuidanceTreeUpdateView.as_view(), 
        name="update_guidance_tree"),
]