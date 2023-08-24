from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField

class GuidanceTree(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # TODO: maybe better way to keep a tree?
    position_array_x_axis = ArrayField(models.FloatField())
    position_array_y_axis = ArrayField(models.FloatField())
    parent_array = ArrayField(models.IntegerField(null=True, blank=True))
    example_input_array = ArrayField(models.TextField())
    example_output_array = ArrayField(models.TextField())
    
    # TODO: store how the front positions the flowchart for keeping & showing

class ChatRoom(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    client = models.CharField(max_length=100, blank=True, null=True)

    guidance_tree = models.ForeignKey(GuidanceTree, on_delete=models.DO_NOTHING)
    guidance_tree_node = models.IntegerField(default=0)
    
    recieved_messages = ArrayField(models.TextField(), default=list, blank=True)
    suggested_messages = ArrayField(models.TextField(), default=list, blank=True)
    sent_messages = ArrayField(models.TextField(), default=list, blank=True)
    recieved_messages_timestamp = ArrayField(models.DateTimeField(), default=list, blank=True)
    sent_messages_timestamp = ArrayField(models.DateTimeField(), default=list, blank=True)