from django.conf                import settings
from django.core.mail           import send_mail
from .models                    import Event
from django.contrib.auth.models import User
from django.utils               import timezone
from django.template.loader     import render_to_string
import eventscraper.Venues      as     venues
import math

def send_mailupdate():
    #Create a list of receivers
    receivers = []
    for user in User.objects.all():
        if user.has_perm('eventscraper.receive_emailupdates') and user.email:
            receivers.append(user.email)
    
    #If there are any users that need to receive an email
    if(receivers):
        #Generate email content
        event_list = Event.objects.filter(date__gte=timezone.now()).filter(date_added__gt=timezone.now()-timezone.timedelta(days=7)).filter(date_added__lte=timezone.now()).order_by('date')
        email_body = render_to_string('eventscraper/recent_events_email.html',{'event_list':event_list})
        
        send_mail(
            'Weekly Update Eventscraper :)',
            '',
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=False,
            html_message=email_body,
        )

def store_event(entry,venue):
    try:
        event = Event.objects.get(URL=entry[3])
        primary_key = event.pk
    except:
        event = None
    #Create a new event object in case the new data is unique
    obj, created = Event.objects.get_or_create(
        venue = venue,
        title = entry[0],
        date  = entry[1],
        time  = entry[2],
        URL   = entry[3]
    )
    #The data of the event must have been updated in case a new object was created; delete the old one
    if created and event:
        Event.objects.get(pk=primary_key)
        
def scrape_events():
    #Call functions to parse the RSS feeds or websites
    for event in venues.BoerderijLoader():
        store_event(event,'Boerderij')
    for event in venues.AFASLiveLoader():
        store_event(event,'AFAS Live')
    for event in venues.PaardLoader():
        store_event(event,'Paard')
    for event in venues.ParadisoLoader():
        store_event(event,'Paradiso')
    for event in venues.ZiggoDomeLoader():
        store_event(event,'Ziggo Dome')
    for event in venues.Tilburg013Loader():
        store_event(event,'Tilburg 013')
    for event in venues.MelkwegLoader():
        store_event(event,'Melkweg')
    for event in venues.ArenaLoader():
        store_event(event,'Arena')
    for event in venues.LuxorLiveLoader():
        store_event(event,'Luxor Live')
    for event in venues.GelredomeLoader():
        store_event(event,'Gelredome')    
    for event in venues.SteckLoader():
        store_event(event,'STECK')    
    for event in venues.CarreLoader():
        store_event(event,'Carré')   
    for event in venues.TivoliLoader():
        store_event(event,'Tivoli') 
