from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from articles.models import Article
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = "articles.html"

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "article.html"


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'body']
    login_url = "login"
    context_object_name = 'article'
    template_name = 'article_edit.html'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    login_url = "login"
    context_object_name = 'article'
    template_name = "article_delete.html"
    success_url = reverse_lazy('articles')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Article
    fields = ['title', 'body']
    context_object_name = 'article'
    template_name = 'article_new.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



