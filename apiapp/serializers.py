from rest_framework import serializers
from .models import Student,Church

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=(
            'name','age'
        )
        
class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Church
        fields=(
            'id','name','founder'
        )
    id=serializers.IntegerField(label="Enter Book Id")
    name=serializers.CharField(label="Enter Church/Fellowship Name")
    founder=serializers.CharField(label="Enter the name of the Founder")
    
            