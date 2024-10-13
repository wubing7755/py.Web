from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

# Create your views here.

def index(request):
    """
    首页
    """
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": lastest_question_list,
        "request_context": request,
    }
    return render(request, "polls/index.html", context)
    
def details(request, question_id):
    """
    问题详情页
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Qustion does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    """
    问题结果页
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    """
    投票处理器
    """
    return HttpResponse("You're voting on question %s." %question_id)