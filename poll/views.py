from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from matplotlib.style import context
from django.shortcuts import render
from .models import question
# Create your views here.
def index(request):
    latest_question_list = question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('poll/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    #output = ' ,'.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context,request))
def detail(request, questoin_id):
    try:
        question = question.objects.get(pk=question_id)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'poll/detail.html',{'question':question})
def results(request,question_id):
    response = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse(response % question_id)