from django.conf.urls import patterns, include, url
from django.contrib import admin

from .api import CoordinateList


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', CoordinateList.as_view(), name='coordinate-list'),
    url(r'^admin/', include(admin.site.urls)),
)
