from django.test import TestCase

# Create your tests here.
from .prompt import OpenaiResponse
from bamie.models import GuidanceTree, ChatRoom

guidance_tree = GuidanceTree.objects.all()[0]

print(OpenaiResponse("what can I do", guidance_tree.children_templates(0)))