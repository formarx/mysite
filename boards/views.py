from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Post, Category


# Create your views here.
class ListView(generic.ListView):
    model = Post
    template_name = 'boards/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        category = self.request.GET.copy().get('category', 'news')
        # ERROR if category is not correct
        catenum = Category.objects.filter(name=category)[0].id
        return Post.objects.filter(category=catenum).order_by('-date')[:20]
