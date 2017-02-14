from bs4      import BeautifulSoup
from datetime import datetime
import requests, ssl, feedparser

def ZiggoDomeLoader():
    import locale
    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch

    URL = 'https://www.ziggodome.nl/agenda'
    container = []
   
    #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").find('div',attrs={'class':'agenda_overview '}).findAll('a',href=True):
        #Abstract some information
        event_status = link.find('span',attrs={'class':'event_status'}).text
        genre        = link.find('span',attrs={'class':'genre'}).text

        url = link['href']
        #open the event page
        event_data = BeautifulSoup(requests.get(url).content,"html.parser").find('div',attrs={'class':'titlebar'})
        
        date  = event_data.find('h2',attrs={'class':'event_date'}).text
        date_time  = datetime.strptime(date.strip(),'%A %d %B %Y')
        
        #TODO: Abstract starting time from event page

        container.append([event_data.find('h1',attrs={'class':'event_title'}).text,
                          date_time.date(),
                          'time',
                          url])

    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
    return container
   
def Paardloader(URL):
    feed = feedparser.parse(URL)
    container = []
    #Loop over the events
    for event in feed['entries']:
        container.append([event['title'].split(' ')[-1],
                         datetime.strptime(event['date'],'%a, %d %b %Y %H:%M:%S %z').date(),
                         datetime.strptime(event['time'],'%H:%M').time(),
                         event['link']])
    return container
    
def ParadisoLoader(URL):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
        
    feed = feedparser.parse(URL)
    container = []
    #Loop over the events

    import locale
    try: #Rick
        print('Rick')
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        print('Sander')
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch

    for event in feed['entries']:
        info       = event['title'].split(' - ')
        date_time  = datetime.strptime(info[0],'%A %d %B %Y %H:%M')
    
        container.append([info[1],date_time.date(),date_time.time(),event['link']])
    
    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
    return container

#Call functions to parse the RSS feeds
paard_container     = Paardloader('http://www.paard.nl/programme/rss/lang/nl')
paradiso_container  = ParadisoLoader('https://www.paradiso.nl/rss.xml')
ziggodome_container = ZiggoDomeLoader()

print(len(paard_container),len(paradiso_container),len(ziggodome_container))