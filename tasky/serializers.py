from rest_framework import serializers
from .models import Task 

#Creating a serializer class for the Task models 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
    