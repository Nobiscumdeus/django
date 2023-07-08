from django.shortcuts import render

##Here we will import requests needed for the collect function 
import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
@api_view(['GET'])
def getData(request):
    item=Item.objects.all()
    serializer=ItemSerializer(item,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
Dealing with Fetching data from an outer APi with ###requests### in django
First of all, install requests in this environment with pip install requests
"""
def collect(request):
    try:
        headers = {"X-RapidAPI-Key": "SIGN-UP-FOR-KEY","X-RapidAPI-Host": "covid-193.p.rapidapi.com"}
        url="https://covid-193.p.rapidapi.com/countries"
        response=requests.get(url,headers=headers)
        data =response.json()
    
        return render(request,'api/collect.html',{'data':data})
    except requests.exceptions.RequestException as e:
        error_message="Error Occurred while making the APi Requests {}".format(str(e))
    
    except Exception as e:
        error_message='An error occurred {}'.format(str(e))
        return render(request,'api/collect.html',{'error_message':error_message},status=500)

