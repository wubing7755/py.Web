from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.db.models import F
from django.urls import reverse

from .models import Question, Choice

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question":question})

def vote(request, question_id):
    """
    投票处理器
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id)))