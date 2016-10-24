from django.shortcuts import render
from blog.models import Article
# Create your views here.


def index(request):
    articles=Article.objects.filter(is_active=True)
    return render(request,'index.html', {'articles': articles})

def get_article(request, article_id):
    article=Article.objects.get(id=article_id)
    return render(request, 'article_page.html', {'article': article})