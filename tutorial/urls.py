from django.urls import path
from . import views
app_name='tutorial'
urlpatterns=[
    path('',views.Index,name="Index"),
    path('articles/<int:year>/',views.year_archive),
    path('results/',views.result,name="result"),
    path('results/<int:out>/',views.delete,name="delete"),
    path('index',views.index,name='index'),
    #example tutorial/5
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/vote',views.vote,name='vote'),
    path('<int:question_id>/vote_results/',views.vote_results,name='vote_result'),
    

]