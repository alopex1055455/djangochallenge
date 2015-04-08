from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', url(r'^threeCategories/', include('threeCategories.urls')),
url(r'^admin/', include(admin.site.urls)),)
