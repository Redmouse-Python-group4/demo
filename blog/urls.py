from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'article/([0-9]+)/$', views.get_article, name="get_article"),
    url(r'article/([0-9]+)/edit/$', views.article_edit),
    url(r'category/([0-9]+)/$', views.get_category_article, name="get_category_article"),
    url(r'comments/([0-9]+)/$', views.create_comments, name="set_comment"),
    url(r'rating/([0-9]+)/$', views.set_rating, name="set_rating"),
    url(r'about_me/$', views.AboutMe.as_view(),name="about_me" ),
    url(r'$', views.index, name="index"),

]