from django.shortcuts     import render
from django.views.generic import View, ListView
from .models              import Event
from .scripts             import import_file,scrape_events
   
# class Index(View):
    # def get(self, request, *args, **kwargs):
        # show_text = "Soon this will be the Event Scraper page!!"
        # return render(request,'eventscraper/events.html')

class EventListView(ListView):
    model         = Event
    template_name = 'eventscraper/event_list.html'
    ordering      = 'date'
    
    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        
        # #Import CSV
        # import_file('C:/Users/svanl/Dropbox/Python and Django Tools/LvM_Scraper/events.csv')
        
        #Run script for scraping events and loading it in the database
        # scrape_events()
        
        return context