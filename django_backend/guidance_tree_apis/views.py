from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from knox.auth import TokenAuthentication

from bamie.models import GuidanceTree


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

    def create(self, request):
        # TODO: create a guidance tree with owner as user
        pass
    def list(self, request):
        # TODO: list all of the user's guidance trees
        pass
    def detail(self, request):
        # TODO: get the guidance tree by pk the user must be the owner of the guidance tree
        pass
    def update(self, request):
        # TODO: update the guidance tree with the given pk user must be the owner of the guidance tree         
        pass