"""tlogblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article.views import ArticleListView
from article.views import ArticleSitemap
from django.contrib.sitemaps.views import sitemap
from article.feeds import LatestEntriesFeed
from django.views.generic.base import TemplateView
from article import views

admin.autodiscover() #use this to instantiate admin

sitemaps = {
    'Article': ArticleSitemap
}

urlpatterns = [
    url(r'^json/', include(admin.site.urls)),
    url(r'^$',views.articlesview, name = 'articlesview'),
    url(r'^articles/$',views.articles, name = 'articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$',views.article, name = 'article'),
    url(r'^create/$', views.create, name='create'),
    url(r'^newquote/$', views.newquote, name='newquote'),
    ##################################################################################
    #user registration
    url(r'^accounts/register/$', views.register_user, name = 'register_user'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),

    ############################################################################
    #Authentication URL
    url(r'^articlesadmin/accounts/login/$', views.login, name = 'login'),
    url(r'^accounts/auth/$', views.auth_view, name = 'auth_view'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name = 'loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    #########################################################################
    url(r'^articlelist/$', ArticleListView.as_view(), name='article-list'),
    url(r'^feed/$', LatestEntriesFeed()),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',content_type ='text/plain')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

