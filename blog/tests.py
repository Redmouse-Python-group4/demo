from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

# Create your tests here.
from blog.models import Category, Article, Reting


class ArticleTest(TestCase):
    def test_get_rating_in_article_without_raiting(self):
        category = Category(name="kjkjkj", slug="kjdkfj")
        category.save()
        article =Article(title='kejrkej', body='lksdlksl', category=category)
        article.save()
        self.assertEqual(article.get_rating(), 0)


    def test_get_rating_in_article_with_one_raiting(self):
        category = Category(name="kjkjkj", slug="kjdkfj")
        category.save()
        article =Article(title='kejrkej', body='lksdlksl', category=category)
        article.save()
        rating = Reting(article=article, mark=1)
        rating.save()
        self.assertEqual(article.get_rating(), 1)

    def test_get_rating_in_article_with_two_raiting(self):
        category = Category(name="kjkjkj", slug="kjdkfj")
        category.save()
        article =Article(title='kejrkej', body='lksdlksl', category=category)
        article.save()
        rating = Reting(article=article, mark=1)
        rating.save()
        rating = Reting(article=article, mark=5)
        rating.save()
        self.assertEqual(article.get_rating(), 6)

class ArticleViewsTest(TestCase):

    def test_index_page(self):
        client = Client()
        response= client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(type(response.context), list)
    def test_article_page_without_article(self):
        client = Client()
        response= client.get(reverse('blog:get_article', args=[12,]))
        self.assertEqual(response.status_code, 404)

    def test_article_page_with_article(self):
        client = Client()
        category = Category(name="kjkjkj", slug="kjdkfj")
        category.save()
        article = Article(title='kejrkej', body='lksdlksl', category=category)
        article.save()
        response= client.get(reverse('blog:get_article', args=[article.id,]))
        self.assertEqual(response.status_code, 200)