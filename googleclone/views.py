from django.shortcuts import render
from django.http import HttpResponse; import requests; from bs4 import BeautifulSoup
#For python web scraping , we need beautifulsoup4, bs4 lxml, requests
def index(request):   
    return HttpResponse('You are welcome ')
    
def search(request):
    return render(request,'googleclone/search.html')
def scrape(request):
    url="https://chasfatprojects.netlify.app"
    response=requests.get(url)
    soup=BeautifulSoup(respose.content,"html.parser")
    headings=soup.find_all('h1')
    data=[heading.text for heading in headings]
    return render(request,'googleclone/scrape.html',{'data':data})
    
      
     



