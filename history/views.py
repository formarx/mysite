from django.shortcuts import render
from django.views import generic

from .models import History

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'history/index.html'
    context_object_name = 'history_list'

    def get_queryset(self):
        return History.objects.all().order_by('-history_date')[:20]