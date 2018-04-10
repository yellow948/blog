# -*- coding:utf8 -*-
from django.conf.urls import url, include
from django.contrib import admin

from myBlog.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('myBlog.urls')),
    url(r'^$', IndexView.as_view()),# 先后顺序
]
