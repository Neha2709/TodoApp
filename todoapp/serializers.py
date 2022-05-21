from rest_framework import serializers
from .models import TodoItem

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id','content','status','ETA')