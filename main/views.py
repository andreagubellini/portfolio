from django.shortcuts import render
from . models import Article
from django.views.generic import ListView
from django.utils import timezone


def index(request):
    return render(request, 'main/index.html')

def volevi(request):
    return render(request, 'main/volevi.html')

class ArticleListView(ListView):
    model = Article
    template_name = 'blog'
    paginate_by = 100
    
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def post(self, request):
        post_title = Article.title # or something which you want to do.
        context = {
        'post_list': post_title,
        }
        return render(request, 'index.html', context)