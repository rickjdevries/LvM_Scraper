from django.conf.urls import url

from . import views

app_name = 'event_scraper'
urlpatterns = [
    # url(r'^$', views.Index.as_view(), name='index'),
    url(r'^event_list/$', views.EventListView.as_view(), name='event_list'),
]