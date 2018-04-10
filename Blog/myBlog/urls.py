# -*- coding:utf8 -*-
from django.conf.urls import url
from .views import PushArticleView, ArticleShowView, TypeView, SearchView


urlpatterns = [
    url(r'^push/$', PushArticleView.as_view()),
    url(r'^article/(.+)/$', ArticleShowView.as_view()),
    url(r'^type/(.*?)/$', TypeView.as_view()),
    url(r'^search/$', SearchView.as_view()),
]
