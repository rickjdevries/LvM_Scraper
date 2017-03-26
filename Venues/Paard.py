from datetime import datetime
import feedparser

def PaardLoader():
    URL = 'http://www.paard.nl/programme/rss/lang/nl'

    feed = feedparser.parse(URL)
    container = []
    #Loop over the events
    for event in feed['entries']:
        container.append([event['title'][12:].strip(),
                         datetime.strptime(event['date'],'%a, %d %b %Y %H:%M:%S %z').date(),
                         datetime.strptime(event['time'],'%H:%M').time(),
                         event['link']])
    return container