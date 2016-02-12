from django.conf.urls import patterns, url

from slack import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
