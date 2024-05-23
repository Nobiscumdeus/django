from django.shortcuts import render,redirect

# Create your views here.

#API View for Sensor Data
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer
#Sending with Ajax
from django.http import JsonResponse,HttpResponseNotAllowed
#Class Based View Authentication and Authorization 
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm, UserLoginForm
from django.views import View
from django.contrib.auth import logout
#Authorization purpose 
from django.contrib.auth.decorators import login_required


class UserRegistrationView(CreateView):
    form_class=UserRegistrationForm
    template_name='sensor/register.html'
    success_url=reverse_lazy('sensor:login')
    
class UserLoginView(LoginView):
    form_class=UserLoginForm
    template_name='sensor/login.html'
    success_url=reverse_lazy('sensor:sensor_data_list')
    
class UserLogOutView(View):
    def get(self, request, *args, **kwargs):
        # Redirect to the home page or another page for GET requests
        return redirect('sensor:login')

    def post(self, request, *args, **kwargs):
        logout(request)
        # Redirect to a success page or another page after logout
        return redirect('sensor:login')

    def http_method_not_allowed(self, request, *args, **kwargs):
        # Return a 405 Method Not Allowed response for unsupported methods
        return HttpResponseNotAllowed(['POST'])
        
    


#API View for Sensor Datafrom django.shortcuts import render

# Create your views here.

#API View for Sensor Datafrom django.shortcuts import render

# Create your views here.

#API View for Sensor Datafrom django.shortcuts import render

# Create your views here.

#API View for Sensor Datafrom django.shortcuts import render

# Create your views here.

#API View for Sensor Data
@api_view(['POST'])
def submit_data(request):
    if request.method=='POST':
        serializer=SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response({"status":"error","message":"Only POST method is allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@login_required    
def sensor_data_list(request):
    sensor_data=SensorData.objects.all().order_by('-timestamp')
    return render(request,'sensor/data_list.html',{'sensor_data':sensor_data})



#To send data through json & Ajax 
@login_required
def sensor_data_json(request):
    sensor_data = SensorData.objects.all().order_by('-timestamp')
    data_list = [
        {
            'timestamp': data.timestamp,
            'sensor_id': data.sensor_id,
            'sensor_type': data.sensor_type,
            'value': data.value,
            'unit': data.unit,
            'location': data.location,
            'status': data.status,
            'battery_level': data.battery_level,
            'calibration_date': data.calibration_date,
            'environment_context': data.environment_context,
            'data_quality': data.data_quality,
        }
        for data in sensor_data
    ]
    return JsonResponse(data_list, safe=False)
        
        