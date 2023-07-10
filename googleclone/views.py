from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup; 
from .forms import SearchForm;
#For python web scraping , we need beautifulsoup4, bs4 lxml, requests
#from django.core.email import send_mail


"""
def mail_sending(request):
    send_mail('Hey, this is from Chasfat Projects',
              'Subject :Tutorial on Django mails',
              'From: emmanueladeola990@gmail.com',
              ['samuel@gmail.com','fhehehe@gmail.com'],
              fail_silently=False)
    return render(request,'homeemail.html')"""

def search_view(request):
    if(request.method=='POST'):
        form=SearchForm(request.POST)
        if(form.is_valid()):
            query=form.cleaned_data['query']
            url = f'https://www.ask.com/search?q={query}'
            response=requests.get(url)
            soup=BeautifulSoup(response.text,'html.parser')
            search_results=[]
            for result in soup.find_all('div',{'class':'result'}):
                title=result.find('h3').text
                url=result.find('a')['href']
                description=result.find('p').text
                search_results.append({'title':title,'url':url,'description':description})
            return render(request,'googleclone/search.html',{'result':result})
    else:
        form=SearchForm()
        return render(request,'googleclone/search.html',{'form':form})
                
def index(request):   
    return HttpResponse('You are welcome ')    
def search(request):   
    if request.method=="POST":
        search=request.POST['search']
        url='https://www.ask.com/web?q='+search
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'lxml')
        result_list=soup.find_all('div',{'class':'PartialSearchResults-item'})
        final_result=[]
        for result in result_list:
            result_title=result.find(class_='PartialSearchResults-item-title').text
            result_url=result.find('a').get('href')
            
            result_description=result.find(class_='PartialSearchResults-item-abstract').text
            final_result.append((result_title,result_url,result_description))
            
        context={
            'final_result':final_result
        }
        return render(request,'googleclone/clone.html',context)
    else:
        return(request,'googleclone/clone.html')
    
#For sending mails 
        
            
            
        
        
   
   
   
    
    return render(request,'googleclone/search.html')


def scrape(request):
    url="https://chasfatprojects.netlify.app"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    headings=soup.find_all('h1')
    data=[heading.text for heading in headings]
    return render(request,'googleclone/scrape.html',{'data':data})

#A function serving for counting words
def count(request):
    return render(request,'googleclone/counter.html')
def counter(request):
    tex=request.GET['text']
    amount=len(tex)
    return render(request,'googleclone/counter.html',{'amount':amount})
