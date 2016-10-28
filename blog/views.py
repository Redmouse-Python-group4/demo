from blog.forms import CommentsForm, ArticleForm
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Comment
# Create your views here.


def index(request):
    articles=Article.objects.filter(is_active=True)
    return render(request, 'blog/index.html', {'articles': articles})

def get_article(request, article_id):
    # article=Article.objects.get(id=article_id)
    article=get_object_or_404(Article,id=article_id)
    form = CommentsForm()
    comments = Comment.objects.filter(article_id=article, enable=True)
    return render(request, 'blog/article_page.html',
                  {'article': article, 'comments': comments , 'form': form})

def article_edit(request, id):
    article=Article.objects.get(pk=id)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method=='POST':
        if form.is_valid():
            form.save()
    return render(request, "blog/form_edit.html", {'form': form})


def create_comments(request, article_id):
    article=Article.objects.get(pk=article_id)
    form = CommentsForm(request.POST)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.article_id = article
        obj.author = request.user
        obj.save()
        return redirect('/article/%s'%article.id)
    return redirect('/')