"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hello_app import views
from test import views as test_views
from movie import views as movie_views
from blog import views as blog_views
from haystack.views import SearchView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^forms/$', views.contact),
    url(r'^contact/thanks/$',views.thanks),
    url(r'^test123456/$',test_views.testdr,name='test123'),
    url(r'^search/(?P<keys>\w+)/$',movie_views.search,{'var':'hello'}),
    url(r'^search/en/(?P<keys>\w+)/$',movie_views.search,{'var':'hi'}),
    url(r'^search_whoosh/$',movie_views.search_whoosh,name='search_whoosh'),
    url(r'^searchs/$',SearchView()),


    # url(r'^mail/$', views.mail),




]
