from django.conf.urls import patterns, url
from threeCategories.models import category
from threeCategories import views

urlpatterns = patterns('',url(r'^$', views.index, name = 'index'), url(r'^results/$',views.detail,name = 'detail'),)

