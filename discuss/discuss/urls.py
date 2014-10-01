from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Include URLs from converse/urls.py
    url(r'^', include('discuss.converse.urls')),

    # Enable the built-in django admin page
    url(r'^admin/', include(admin.site.urls)),
)
