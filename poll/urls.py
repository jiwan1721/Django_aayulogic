from django.urls import path
from . import views
from .views import index

urlpatterns =[
    path('',views.index,name='index'),
    path('/poll/5',views.detail,name='detail'),
    path('/poll/5/results',views.results,name='detail'),
    path('/polls/5/vote',views.vote,name ='vote'),  
]
