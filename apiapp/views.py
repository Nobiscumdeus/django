from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import csv

from .serializers import StudentSerializer, ChurchSerializer
from .models import Student, OndoDoctors,Church

def export_to_csv(request):
    profiles=Church.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment;filename=profile_export.csv'
    writer=csv.writer(response)
    writer.writerow(['id','name','founder'])
    profile_fields=profiles.values_list('id','name','founder')
    for profile in profile_fields:
        writer.writerow(profile)
    return response
    

class firstView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Student.objects.all()
        serializer=StudentSerializer(qs,many=True)
        return Response(serializer.data)

class ChurchAPIView(APIView):
    serializer_class=ChurchSerializer
    def get(self,request):
        churches=Church.objects.all().values()
        return Response({'Message':'Details of Churches','churches':churches})
    
    def post(self,request):
        print('Request data is: ',request.data)
        serializer_object=ChurchSerializer(data=request.data)
        if(serializer_object.is_valid()):
            
        
            Church.objects.create(id=serializer_object.data.get('id'),
                                name=serializer_object.data.get('name'),
                                founder=serializer_object.data.get('founder'))
            church=Church.objects.all().filter(id=request.data['id']).values()
            return Response({'Message':'Details of newly added Church(es)','church':church})
        
class OndoDoctorsAPIView(APIView):
    def get(self,request):
        ondodoctors=OndoDoctors.objects.all().values()
        return Response({'Message':'Details of Ondo Doctors','doctorsdetails':ondodoctors})
    
    def post(self,request):
        OndoDoctors.objects.create(id=request.data['id'],
                                   name=request.data['name'],
                                   birth_day=request.data['birth_day'],
                                   specialty=request.data['specialty'],
                                   local_govt=request.data['local_govt'],
                                   medical_school=request.data['medical_school'],
                                   hospital_worked=request.data['hospital_worked'],
                                   positions=request.data['positions'],
                                   awards=request.data['awards']
                                   )
        specificdoctors=OndoDoctors.objects.all().filter(id=request.data['id']).values()
        return Response({'Message':'Details of the Doctor Added','specific_doctor':specificdoctors})