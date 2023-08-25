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
    
    def children_templates(self, id):
        """
            returns a list of tuples of the children of the node with index id
            each tuple containing a example_input and an example_output
        """
        children = []
        for parent, indx in enumerate(self.parent_array):
            if parent == id:
                children.append((self.example_input_array[indx], self.example_output_array[indx]))
        return children

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