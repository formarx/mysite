
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

from polls import models as pollsModels
from history import models as historyModels


def MainPage(request):
    history_list = historyModels.History.objects.all().order_by('-history_date')[:20]
    context = {'history_list': history_list, }

    latest_question_list = pollsModels.Question.objects.all().order_by('-pub_date')[:5]
    context['latest_question_list'] = latest_question_list

    return render(request, 'home.html', context)

