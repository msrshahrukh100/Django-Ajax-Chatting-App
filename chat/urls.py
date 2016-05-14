from django.conf.urls import url,include
from .views import *
urlpatterns = [
    url(r'^$',home , name="home"),
    url(r'^dashboard/$',dashboard , name="dashboard"),
    url(r'^logout/$',logout_view , name="logout"),
    url(r'^chat/(?P<id>\d+)$',chatting , name="chat"),


]
