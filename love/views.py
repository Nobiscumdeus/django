
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.response import Response

from .models import Article





# Create# your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse("This is first function powered by Nobiscumdeus ")
def welcome(request):
    return HttpResponse("Hello world , welcome to Django by Nobiscumdeus ")

@api_view(['GET','POST'])
def article_list(request,format=None):
    #get all the drinks
    #serialize all the drinks
    #return a json 
    if request.method =='GET':
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)
        #If you intend to return as a dictionary, do what's below
        #return JsonResponse({"articles":serializer.data},safe=False)
    if request.method =='POST':
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def article_details(request,id,format=None):
    try:
        article=Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
       
    if request.method =='GET':
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,statUs=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
