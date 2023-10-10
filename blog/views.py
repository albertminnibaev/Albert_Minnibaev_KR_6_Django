from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.forms import ArticleForm
from blog.models import Article


# Create your views here.

class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Статьи блога'
    }


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:article')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:article')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article')


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.quantity += 1
        self.object.save()
        return self.object


def toggle_activity(request, pk):
    article_item = get_object_or_404(Article, pk=pk)
    if article_item.sign:
        article_item.sign = False
    else:
        article_item.sign = True

    article_item.save()

    return redirect(reverse('blog:article'))
