from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from knox.auth import TokenAuthentication

from bamie.models import GuidanceTree
from .serializers import GuidanceTreeSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination

class NoPagination(PageNumberPagination):
    page_size = None

class GuidanceTreeAPIViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = GuidanceTree.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        position_array=[],
                        parent_array=[],
                        example_input_array=[],
                        example_output_array=[],)
        
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

    def create(self, request):
        # TODO: create a guidance tree with owner as user
        serializer = GuidanceTreeSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        user = request.user
        if pk is not None:
            guidance_tree = get_object_or_404(self.queryset.filter(owner=user), pk=pk)
        else:
            user_guidance_tree_list = self.queryset.filter(owner=user)
            if user_guidance_tree_list.count() == 0:
                self.create_empty_tree_for_user()
            guidance_tree = self.queryset.filter(owner=user)[0]
        serialized_guidance_tree = GuidanceTreeSerializer(guidance_tree)
        return Response(serialized_guidance_tree.data, status=200)
    
    def list(self, request):
        # TODO: list all of the user's guidance trees
        user = request.user
        list_view = ListAPIView.as_view(queryset=self.queryset.filter(owner=user),
                                        serializer_class=GuidanceTreeSerializer,
                                        # no pagination ??
                                        )

class GuidanceTreeUpdateView(UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = GuidanceTreeSerializer
    def get_queryset(self):
        return GuidanceTree.objects.all().filter(owner=self.request.user)