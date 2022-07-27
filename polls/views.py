from django.shortcuts import render,get_object_or_404
from django.views import generic

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice,Adeolas
from django.urls import reverse

def love(request):
    latest_question_list=Question.objects.order_by('-pub_date')
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context,request))
   # output=',  '.join([q.question_text for q in latest_question_list])
   # return HttpResponse(output)
   
   
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    #return HttpResponse("You're looking at question %s."%question_id)


def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
    #response="You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist()):
        #Redisplay the question voting form 
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #Always return a HttpResponseRedirect after successfully dealing 
        #with POST data. This prevents data from being posted twice if a 
        #use hits the back button 
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
        
    
    #return HttpResponse("You're voting on question %s."%question_id)

#Trying bootstrap
def bootstrap(request):
    template=loader.get_template('polls/trybootstrap.html')
    return HttpResponse(template.render())

'''def adeolas(request):
    mine=Adeolas.objects.all().values()
    output=""
    for x in mine:
        output+=x['firstname']+'\n'+'\n'+'\n'
    
    return HttpResponse(output)
    '''

def adeolas(request):
    mine=Adeolas.objects.all().values()
    template=loader.get_template('polls/adeolas.html')
    context={
       'mine':mine
   }
    return HttpResponse(template.render(context,request))
 
 
def addAdeola(request):
    template=loader.get_template('polls/addadeolas.html')
    return HttpResponse(template.render({},request))
#We add the query for adding the records now to the database

def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    update=Adeolas(firstname=x,lastname=y)
    update.save()
    return HttpResponseRedirect(reverse('adeolas'))
#We want to work with the sss1 database so we import it first
from .models import sss1
def senior1(request):
    records=sss1.objects.order_by('fullnames')
    template=loader.get_template('polls/sss1.html')
    context={
        'records':records,
    }
    return HttpResponse(template.render(context,request))
    #output=',  '.join([q.fullnames for q in records])
    #return HttpResponse(output)
    
def check(request):
    template=loader.get_template('polls/check.html')
    context={
    'x':['Apple','Banana','Cherry'],
    'y':['Apple','Banana','Cherry'],
    }
    return HttpResponse(template.render(context,request))