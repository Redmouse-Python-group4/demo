from django.core.urlresolvers import reverse

from blog.forms import CommentsForm, ArticleForm, RaitingForm
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Comment, Category
from django.views.generic import TemplateView, View
# Create your views here.


def index(request):
    articles=Article.objects.filter(is_active=True)
    return render(request, 'blog/index.html', {'articles': articles})

def get_category_article(request, category_id):
    category=get_object_or_404(Category, pk=category_id)
    articles=Article.objects.filter(is_active=True, category=category)
    return render(request, 'blog/index.html', {'articles': articles})

def get_article(request, article_id):
    # article=Article.objects.get(id=article_id)
    article=get_object_or_404(Article,id=article_id)
    form = CommentsForm()
    rating_form = RaitingForm()
    comments = Comment.objects.filter(article_id=article, enable=True)
    return render(request, 'blog/article_page.html',
                  {'article': article, 'comments': comments , 'form': form,  'rating_form': rating_form})

def article_edit(request, id):
    article=Article.objects.get(pk=id)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method=='POST':
        if form.is_valid():
            form.save()
    return render(request, "blog/form_edit.html", {'form': form})

class ArticleView(View):
    template_name = "blog/form_edit.html"

    def get(self):
        article = Article.objects.get(pk=id)
        form = ArticleForm(request.POST or None, instance=article)

    def post(self, *args):
        form = ArticleForm(args or None, instance=article)
        if form.is_valid():
            form.save()

def create_comments(request, article_id):
    article=Article.objects.get(pk=article_id)
    form = CommentsForm(request.POST)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.article_id = article
        obj.author = request.user
        obj.save()
        return redirect(reverse('blog:get_article', args=[article.id]))
    return redirect(reverse('blog:index'))

class AboutMe(TemplateView):
    template_name = 'blog/about_me.html'

def set_rating(request, article_id):
    article = Article.objects.get(pk=article_id)
    form = RaitingForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.article = article
        obj.save()
        return redirect(reverse('blog:get_article', args=[article.id]))
    return redirect(reverse('blog:index'))