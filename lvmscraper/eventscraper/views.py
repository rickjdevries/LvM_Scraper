from django.views.generic       import View, ListView
from django.shortcuts           import redirect
from .models                    import Event
from django.utils               import timezone
from .scripts                   import scrape_events
from django.contrib.auth.mixins import PermissionRequiredMixin
from eventscraper.forms         import SearchForm

class SearchList(PermissionRequiredMixin, ListView):
    form_class          = SearchForm
    model               = Event
    permission_required = ('eventscraper.view_eventscraper')
    def get_context_data(self, **kwargs):
        context = super(SearchList, self).get_context_data(**kwargs)
        if 'action' in self.request.GET and self.request.GET['action'] == 'process_form':
            context['form'] = self.form_class(self.request.GET)
        else:
            context['form'] = self.form_class()
        return context
        
class EventListView(SearchList):
    template_name = 'eventscraper/event_list.html'
    
    def get_queryset(self):
        event_set = Event.objects.filter(date__gte=timezone.now()).order_by('date')
        if 'action' in self.request.GET and self.request.GET['action'] == 'process_form':
            form = self.form_class(self.request.GET)
            if form.is_valid():
                search_word = form.cleaned_data['search_word']
                #Filtering of the table based on the input from the search form
                if search_word:
                    return event_set.filter(title__icontains=search_word)
        return event_set
      
class RecentlyAddedEventsView(SearchList):
    template_name = 'eventscraper/recent_events_list.html'

    def get_queryset(self):
        event_set = Event.objects.filter(date__gte=timezone.now()).filter(date_added__gt=timezone.now()-timezone.timedelta(days=7)).filter(date_added__lte=timezone.now()).order_by('-date_added','date')
        if 'action' in self.request.GET and self.request.GET['action'] == 'process_form':
            form = self.form_class(self.request.GET)
            if form.is_valid():
                search_word = form.cleaned_data['search_word']
                #Filtering of the table based on the input from the search form
                if search_word:
                    return event_set.filter(title__icontains=search_word)
        return event_set

class VenueView(PermissionRequiredMixin,ListView):
    model               = Event
    template_name       = 'eventscraper/event_list.html'
    permission_required = ('eventscraper.view_eventscraper')
    
    def get_context_data(self, **kwargs):
        context = super(VenueView, self).get_context_data(**kwargs)
        #Only show the events from today on
        context['event_list'] = Event.objects.filter(venue=self.kwargs['venue']).filter(date__gte=timezone.now()).order_by('date')
        #Return the context
        return context
        
class VenueListView(PermissionRequiredMixin,ListView):
    model               = Event
    template_name       = 'eventscraper/venue_list.html'
    permission_required = ('eventscraper.view_eventscraper')
    
    def get_context_data(self, **kwargs):
        context = super(VenueListView, self).get_context_data(**kwargs)
        #Only show the events from today on
        context['venue_list'] = Event.objects.values('venue').distinct()
        #Return the context
        return context
        
class UpdateDatabase(PermissionRequiredMixin,View):
    permission_required = ('eventscraper.view_eventscraper')
    
    def get(self, request, *args, **kwargs):
        #Run script for scraping events and loading it in the database
        scrape_events()
        #Redirect to the event listview
        return redirect('event_scraper:event_list')