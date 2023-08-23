from django.test import TestCase

# Create your tests here.
from .models import GuidanceTree
from django.contrib.auth.models import User, Group


guidance_tree = GuidanceTree.objects.create(
    owner=User.objects.all().filter(username="someoneasdf")[0],
    parents_array=[-1, 2],
    example_input_array=['ihiasdf', 'asdfasdf'],
    example_output_array=['asdfasdf', 'asdfkljsadf'],
)

guidance_tree.save()