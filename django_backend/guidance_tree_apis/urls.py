from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.GuidanceTreeAPIViewSet.as_view({
        'post': 'create',
    }), name="create_guidance_tree"),
    path('list/', views.GuidanceTreeAPIViewSet.as_view({
        'get': 'list',
    }), name="list_guidance_tree"),
    path('detail/', views.GuidanceTreeAPIViewSet.as_view({
        'get': 'detail',
    }), name="detail_guidance_tree"),
    path('update/', views.GuidanceTreeAPIViewSet.as_view({
        'put': 'update',
    }), name="update_guidance_tree"),
]