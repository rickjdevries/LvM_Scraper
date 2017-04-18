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
       
def scrape_events():
    #Call functions to parse the RSS feeds
    Boerderij_container  = venues.BoerderijLoader()
    AFAS_container       = venues.AFASLiveLoader()
    paard_container      = venues.PaardLoader()
    paradiso_container   = venues.ParadisoLoader()
    ziggodome_container  = venues.ZiggoDomeLoader()
    Tilburg013_container = venues.Tilburg013Loader()
    melkweg_container    = venues.MelkwegLoader()
    arena_container      = venues.ArenaLoader()
    luxorlive_container  = venues.LuxorLiveLoader()
    gelredome_container  = venues.GelredomeLoader()
    steck_container      = venues.SteckLoader()
    
    Venues = [[Boerderij_container,'Boerderij'],[AFAS_container,'AFAS Live'],[paard_container,'Paard'],[paradiso_container,'Paradiso'],[ziggodome_container,'Ziggo Dome'],[Tilburg013_container,' Tilburg 013'],[melkweg_container,'Melkweg'],[arena_container,'Arena'],[luxorlive_container,'Luxor Live'],[gelredome_container,'Gelredome'],[steck_container,'STECK']]

    for venue in Venues:
        #Loop over the entries
        for entry in venue[0]:
            #Check if the url already exists in the database
            try:
                event = Event.objects.get(URL=entry[3])
            except:
                pass
            
            #Create a new event object in case the new data is unique
            obj, created = Event.objects.get_or_create(
                venue = venue[1],
                title = entry[0],
                date  = entry[1],
                time  = entry[2],
                URL   = entry[3]
            )
            
            #The data of the event must have been updated in case a new object was created; delete the old one
            if created and event:
                event.delete()