# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Article

import time, json


class ArticleShowView(View):
    '''文章显示类'''

    def get(self, request, id):
        return render(request, 'myBlog/article.html')

    def post(self, request, id):
        data = []
        try:
            article = Article.objects.get(id=id)
            the_article = {
                'title': article.title,
                'type': article.type,
                'author': article.author,
                'date': article.date,
                'content': article.content
            }
            data.append(the_article)
            status = 200
            msg = '获取成功'
        except:
            status = 405
            msg = '获取失败'

        return_json = {'status': status, 'msg': msg, 'data': data}
        return HttpResponse(json.dumps(return_json), content_type='application/json')


class PushArticleView(View):
    '''发布文章类'''

    def get(self, request):
        return render(request, 'myBlog/push.html', {'active':'active'})

    def post(self, request):
        title = request.POST.get('title', '')
        author = request.POST.get('author', 'yellow')
        type = request.POST.get('type', '')
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        content = request.POST.get('content', '')
        data = ''
        if type and title and content:
            Article.objects.create(title=title, author=author, type=type, date=date, content=content)
            msg = '发布成功'
            status = 200
            data = '/'
        else:
            msg = '发布失败'
            status = 405

        return_json = {'status': status, 'msg': msg, 'data':data}
        return HttpResponse(json.dumps(return_json), content_type='application/json')


class IndexView(View):
    '''主页类'''

    def get(self, request):
        return render(request, 'myBlog/index.html', {'active':'active'})

    def post(self, request):
        index = request.POST.get('index', 1)
        i = 0; j=5
        for k in range(1, int(index)):
            i += 5;j += 5
        article = Article.objects.all().order_by('-date', '-id')[i:j]
        article_list = []
        if article:
            msg = '获取成功'
            status = 200
            for i in article:
                the_article = {
                    'title': i.title,
                    'type': i.type,
                    'author': i.author,
                    'date': i.date,
                    'content': i.content,
                    'url': '/article/' + str(i.id)
                }
                article_list.append(the_article)
        else:
            msg = '获取失败'
            status = 405
        return_json = {'status': status, 'msg': msg, 'data': article_list}
        return HttpResponse(json.dumps(return_json), content_type='application/json')


class SearchView(View):
    '''搜索类'''

    def post(self, request):
        title = request.POST.get('title')
        article = Article.objects.filter(title__contains=title)
        article_list = []
        if article:
            msg = '获取成功'
            status = 200
            for i in article:
                the_article = {
                    'title': i.title,
                    'type': i.type,
                    'author': i.author,
                    'date': i.date,
                    'content': i.content,
                    'url': '/article/' + str(i.id)
                }
                article_list.append(the_article)
        else:
            msg = '获取失败'
            status = 405
        return_json = {'status': status, 'msg': msg, 'data': article_list}
        return HttpResponse(json.dumps(return_json), content_type='application/json')



class TypeView(View):
    '''分类'''

    def get(self, request, type):
        return render(request, 'myBlog/article_list.html')

    def post(self, request, type):
        index = request.POST.get('index', 1)
        i = 0;
        j = 5
        for k in range(1, int(index)):
            i += 5;
            j += 5
        article = Article.objects.filter(type=type).order_by('-date', '-id')[i:j]
        article_list = []
        if article:
            msg = '获取成功'
            status = 200
            for i in article:
                the_article = {
                    'title': i.title,
                    'type': i.type,
                    'author': i.author,
                    'date': i.date,
                    'content': i.content,
                    'url': '/article/' + str(i.id)
                }
                article_list.append(the_article)
        else:
            msg = '获取失败'
            status = 405
        return_json = {'status': status, 'msg': msg, 'data': article_list}
        return HttpResponse(json.dumps(return_json), content_type='application/json')