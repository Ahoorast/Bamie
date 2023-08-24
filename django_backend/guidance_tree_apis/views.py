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
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.shortcuts import get_object_or_404



# for reference of using restframework generics inside view sets
# from rest_framework.generics import ListAPIView
# from rest_framework.viewsets import ModelViewSet

# class MyModelViewSet(ModelViewSet):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

#     def list(self, request, *args, **kwargs):
#         view = ListAPIView.as_view(queryset=self.filter_queryset(self.get_queryset()))
#         return view(request, *args, **kwargs)

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
    def create(self, request):
        # TODO: create a guidance tree with owner as user
        serializer = GuidanceTreeSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        user = request.user
        guidance_tree = get_object_or_404(self.queryset.filter(owner=user), pk=pk)
        serialized_guidance_tree = GuidanceTreeSerializer(guidance_tree)
        return Response(serialized_guidance_tree.data, status=200)
    def list(self, request):
        # TODO: list all of the user's guidance trees
        user = request.user
        list_view = ListAPIView.as_view(queryset=self.queryset.filter(owner=user),
                                        serializer_class=GuidanceTreeSerializer,
                                        # no pagination ??
                                        )
    def detail(self, request):
        # TODO: get the guidance tree by pk the user must be the owner of the guidance tree
        pass
    def update(self, request):
        # TODO: update the guidance tree with the given pk user must be the owner of the guidance tree         
        pass