from django.forms import fields
from rest_framework import serializers

from .models import Todo, subtodo

class SubTodoSerializer(serializers.Serializer):
    class Meta:
        model = subtodo
        fields = "__all__"

class TodoSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = "__all__"



