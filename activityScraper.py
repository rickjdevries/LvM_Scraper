from bs4      import BeautifulSoup
from datetime import datetime
import requests
import feedparser

#TEST

def ZiggoDomeLoader():
    import locale
    locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch

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

    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    return container
   
def RSSloader(URL,VENUE):
    feed = feedparser.parse(URL)
    container = []
    #Loop over the events
    if VENUE == 'Paradiso':
        import locale
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
        
        for event in feed['entries']:
            info       = event['title'].split(' - ')
            date_time  = datetime.strptime(info[0],'%A %d %B %Y %H:%M')
        
            container.append([info[1],date_time.date(),date_time.time(),event['link']])
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    elif VENUE == 'Paard':
        for event in feed['entries']:
            container.append([event['title'].split(' ')[-1],
                             datetime.strptime(event['date'],'%a, %d %b %Y %H:%M:%S %z').date(),
                             datetime.strptime(event['time'],'%H:%M').time(),
                             event['link']])
    return container

#Call functions to parse the RSS feeds
paard_container     = RSSloader('http://www.paard.nl/programme/rss/lang/nl','Paard')
paradiso_container  = RSSloader('https://www.paradiso.nl/rss.xml','Paradiso')
ziggodome_container = ZiggoDomeLoader()

print(len(paard_container),len(paradiso_container),len(ziggodome_container))