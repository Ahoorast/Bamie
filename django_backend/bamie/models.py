from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField

class GuidanceTree(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # TODO: maybe better way to keep a tree?
    parents_array = ArrayField(
        models.IntegerField(default=-1)
    )
    # TODO: store how the front positions the flowchart for keeping & showing