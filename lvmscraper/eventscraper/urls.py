from django.conf.urls import url

from . import views

app_name = 'event_scraper'
urlpatterns = [
    url(r'^event_list/$', views.EventListView.as_view(), name='event_list'),
    url(r'^added_recently/$', views.RecentlyAddedEventsView.as_view(), name='added_recently'),
    url(r'^event_list/(?P<venue>[\w ]+)/$', views.VenueView.as_view(), name='venue_list'),
    url(r'^venue_list/$', views.VenueListView.as_view(), name='venue_list_view'),
    url(r'^update_database/$', views.UpdateDatabase.as_view(), name='update_database'),
]