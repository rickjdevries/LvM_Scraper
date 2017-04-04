from django.shortcuts     import render, redirect
from django.views.generic import View, ListView
from .models              import Event
from .scripts             import import_file,scrape_events
from datetime             import date
   
class EventListView(ListView):
    model         = Event
    template_name = 'eventscraper/event_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        #Only show the events from today on
        context['event_list'] = Event.objects.filter(date__gte=date.today()).order_by('date')
        #Return the context
        return context
        
class VenueView(ListView):
    model         = Event
    template_name = 'eventscraper/event_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(VenueView, self).get_context_data(**kwargs)
        #Only show the events from today on
        context['event_list'] = Event.objects.filter(venue=self.kwargs['venue']).filter(date__gte=date.today()).order_by('date')
        #Return the context
        return context
        
class VenueListView(ListView):
    model         = Event
    template_name = 'eventscraper/venue_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(VenueListView, self).get_context_data(**kwargs)
        #Only show the events from today on
        context['venue_list'] = Event.objects.values('venue').distinct()
        #Return the context
        return context
        
class UpdateDatabase(View):
    def get(self, request, *args, **kwargs):
        #Run script for scraping events and loading it in the database
        scrape_events()
        #Redirect to the event listview
        return redirect('event_scraper:event_list')