from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField

class GuidanceTree(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # TODO: maybe better way to keep a tree?
    parents_array = ArrayField(models.IntegerField(default=-1))
    example_input_array = ArrayField(models.TextField())
    example_output_array = ArrayField(models.TextField())
    
    # TODO: store how the front positions the flowchart for keeping & showing

class ChatRoom(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    client = models.CharField(max_length=100, blank=True, null=True)

    guidance_tree = models.ForeignKey(GuidanceTree, on_delete=models.DO_NOTHING)
    guidance_tree_node = models.IntegerField(default=0)
    
    recieved_messages = ArrayField(models.TextField())
    suggested_messages = ArrayField(models.TextField())
    sent_messages = ArrayField(models.TextField())
    recieved_messages_timestamp = ArrayField(models.DateTimeField())
    sent_messages_timestamp = ArrayField(models.DateTimeField())