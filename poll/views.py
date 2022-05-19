from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from matplotlib.style import context
from django.shortcuts import get_object_or_404, render      
from .models import Question,Choice
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('poll/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    print(latest_question_list)

    #output = ' ,'.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context,request))
    #return render(request, 'index.html', context)
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'poll/detail.html',{'question':question})
def results(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'poll/results.html',{'question':question})
def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk= request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'poll/detail.html',{
            'question':question,
            'error_message':"you didn't select choice",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results',args=(question.id,)))
   
class index_view(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte = timezone.now()
            ).order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "poll/detail.html"
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class ResultView(generic.DetailView):
    model = Question
    template_name = "poll/results.html"


    