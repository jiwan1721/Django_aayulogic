from django.urls import path,reverse,include
from .views import QuestionSerializer_func,ResultView,DetailView,index_view,vote,results,detail,index,api_root,Choice_serializers_func
from .views import index,question_num,choice_num
# from rest_framework.routers import DefaultRouter
from . import views


# router = DefaultRouter()
# router.register(r'questionSerializer',views.QuestionSerializer_func)

app_name = 'poll'

urlpatterns =[
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name ='vote'),

    path('question',views.QuestionSerializer_func,name = 'question-name'),
    path('question/<int:pk>/',views.question_num,name = 'question_num'),
    # path('api-auth',include('rest_framework.urls')),
    path('api_root',views.api_root),
    path('choice',views.Choice_serializers_func,name = "choices"),
    path('choice/<int:pk>/',views.choice_num,name = "choices_num")
]
