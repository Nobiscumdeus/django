from django.shortcuts import render,get_object_or_404
#To use loader to get the template
from django.template import loader
from django.urls import reverse


# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Article
from .models import Result, Question
def Index(request):
    return HttpResponse("<h1> Now we shall follow Django's documentation to the top </h1>")

def year_archive(request,year):
    #we add year as an argument after the request
    #we sort with pub_date of the article by the __year and its equal to year supplied in the url
    # for an example, a_list=Article.objects.filter(pub_date__year=2022), so the 2022 is coming from the url we specify 
    #as integer in the urls.py
    a_list=Article.objects.filter(pub_date__year=year)
    
    context={'year':year,'article_list':a_list}
    #This will render the request, html page or template specified and it will use the context(which are python variables
    # that will be used in the template file)
    return render(request,'tutorial/year_archive.html',context)

def result(request):
    #A view to result
    results=Result.objects.all()
    context={'results':results}
    return render(request,'tutorial/result.html',context)

def delete(request,out):
    remove=Result.objects.get(id=out)
    remove.delete()
    return HttpResponseRedirect('/tutorial/results/')

#We intend to use loader now instead of hardcoding as it is here
'''def index(request):
    latest_question_text=Question.objects.order_by('-date_published')
    output=' ,'.join([q.question_text for q in latest_question_text ])
    return HttpResponse(output)
    '''
'''
def index(request):
    latest_question_text=Question.objects.order_by('-date_published')
    template=loader.get_template('tutorial/index.html')
    #context below is for the variable taken from the database and what it should represent in the template
    context={
        'latest_question_text':latest_question_text
        #This means latest_question_text should be represented by latest_question_text in our html template
    }
    return HttpResponse(template.render(context,request))
    '''

#another way is to also use the template directly instead of a loader

def index(request):
    latest_question_text=Question.objects.order_by('-date_published')
    context={
        'latest_question_text':latest_question_text
    }
    return render(request,'tutorial/index.html',context)

        
#The next plan is to raise a 404 error that a page does not exist and there are two(2) ways about it fot now 
#1. We can use the seeming long method
#2. We can also use the short method which is get_object_or_404

#The first method 
'''
def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("So sorry, the question you requested does not exist !!!")
    return render(request,'tutorial/detail.html',{'question':question})
    '''

#The second method using get_object_or_404
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'tutorial/detail.html',{'question':question})

#We design the vote to handle the results now 
def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #We can display the voting form again 
        return render(request,'tutorial/detail.html',{'question':question,'error_message':error_message})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        
        #Always use a HttoResponseRedirect so the submission is not avoidably done more than once 
        return HttpResponseRedirect(reverse('tutorial:vote_result',args=(question.id,)))
    
def vote_results(request,question_id):
    question=Question.objects.get(pk=question_id)
    return render(request,'tutorial/vote_results.html',{'question':question})