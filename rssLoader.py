import feedparser
from datetime import datetime
    
def RSSloader(URL,VENUE):
    feed = feedparser.parse(URL)
    container = []
    #Loop over the events
    if VENUE == 'Paradiso':
        import locale
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch
        
        for event in feed['entries']:
            info       = event['title'].split(' - ')
            date_time  = datetime.strptime(info[0],'%A %d %B %Y %H:%M')
        
            container.append([info[1],date_time.date(),date_time.time(),event['link']])
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
    elif VENUE == 'Paard':
        for event in feed['entries']:
            container.append([event['title'].split(' ')[-1],
                             datetime.strptime(event['date'],'%a, %d %b %Y %H:%M:%S %z').date(),
                             datetime.strptime(event['time'],'%H:%M').time(),
                             event['link']])
    return container

#Call functions to parse the RSS feeds
paard_container    = RSSloader('http://www.paard.nl/programme/rss/lang/nl','Paard')
paradiso_container = RSSloader('https://www.paradiso.nl/rss.xml','Paradiso')

print(len(paard_container),len(paradiso_container))