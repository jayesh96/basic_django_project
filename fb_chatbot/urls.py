from django.conf.urls import patterns,url
from fb_chatbot import views
from fb_chatbot import MyQuoteBotView

urlpatterns = patterns('',
	url(r'^$', views.index,name = 'index'),
	url(r'^hi/$', views.hello,name = 'hello'),
	url(r'^hello/hi/$', views.hello,name = 'hello'),
	url(r'^facebook_auth/$', MyQuoteBotView.as_view()))