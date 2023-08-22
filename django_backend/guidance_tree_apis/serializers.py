from knox.serializers import UserSerializer
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from bamie.models import GuidanceTree

class GuidanceTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuidanceTree
        fields = '__all__'