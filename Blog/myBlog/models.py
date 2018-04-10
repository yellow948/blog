# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    author = models.CharField(verbose_name='作者', max_length=20)
    date = models.CharField(verbose_name='发布时间', max_length=20)
    type = models.CharField(verbose_name='文章类型', max_length=20)
    




