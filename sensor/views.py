from django.shortcuts import render

# Create your views here.

#API View for Sensor Data
from rest_framework import status
from rest_framework.descorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer


@api_view(['POST'])
def submit_data(request):
    if request.method=='POST':
        serializer=SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response({"status":"error","message":"Only POST method is allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

    
def sensor_data_list(request):
    sensor_data=SensorData.objects.all()
    return render(request,'sensor/data_list.html',{'sensor_data':sensor_data})
        