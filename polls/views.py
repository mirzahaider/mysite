from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Question


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


def vote(request, question_id):
    return HttpResponse("You're voting for Question %s" % question_id)


def result(request, question_id):
    return HttpResponse("You're looking at the result of Question %s" % question_id)
