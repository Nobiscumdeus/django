from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Question,Choice,TodoList
from django.utils import timezone
from .forms import CreateNewList
#Experimenting with generic views 
class IndexView(generic.ListView):
    #This proivdes the template name that should be displayed 
    template_name='generic/index.html'
    #The latest_question_list here is like saying latest_question_list=Question.objects.all() sort of 
    context_object_name="latest_question_list"
    
    def get_queryset(self):
        '''Return the published questions'''
        return Question.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
class DetailView(generic.DetailView):
    model=Question
    template_name='generic/detail.html'

# We intend to display the results here 
class ResultView(generic.DetailView):
    model=Question
    template_name='generic/results.html'
    
#Vote is where the main portion of our action is performed


def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #We can display the voting form again 
        return render(request,'generic/detail.html',{'question':question,'error_message':"Oops!!! You did not select a choice, please do "})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        
        #Always use a HttoResponseRedirect so the submission is not avoidably done more than once 
        return HttpResponseRedirect(reverse('generic:results',args=(question.id,)))
def home(response):
    if response.method=='POST':
        form=CreateNewList(response.POST)
        
        if form.is_valid():
            n=form.cleaned_data['name']
            t=TodoList(name=n)
            t.save()
            context={
                't':t
            }
            list=TodoList.objects.all()
            return render(response,'generic/formsresult.html',{'list':list})   
    else:
        form=CreateNewList()
        return render(response,'generic/form.html',{'form':form})