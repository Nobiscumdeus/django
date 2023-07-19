from django.contrib import admin
from django.urls import path
from . import views
app_name='polls'

urlpatterns=[
    #ex:/polls/
path('',views.love,name='love'),


#ex:polls/5/
path('<int:question_id>/',views.detail,name='detail'),
#ex:/polls/5/results/
path('<int:question_id>/results',views.results,name='results'),
#ex:/polls/5/vote
path('<int:question_id>/vote',views.vote,name='vote'),

#for bootstrap template
path('bootstrap',views.bootstrap,name='bootstrap'),
path('adeolas',views.adeolas,name='adeolas'),
path('add/',views.addAdeola,name='add'),
path('add/addrecord/',views.addrecord,name='addrecord'),

path('senior1/',views.senior1,name='senior1'),
path('check',views.check,name='check'),

path('paginate',views.QuestionListView.as_view(),name='paginate')
]
