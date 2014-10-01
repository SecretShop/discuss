from django.conf.urls import patterns, url

from .views import TeamList
from .views import PostList


urlpatterns = patterns('',
    url(r'^posts/$', PostList.as_view()),
    url(r'^$', TeamList.as_view()),
)
