from django.conf.urls import url

from . import views

app_name = 'event_scraper'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]