from datetime import datetime
import feedparser

def PaardLoader(URL):
    feed = feedparser.parse(URL)
    container = []
    #Loop over the events
    for event in feed['entries']:
        container.append([event['title'].split(' ')[-1],
                         datetime.strptime(event['date'],'%a, %d %b %Y %H:%M:%S %z').date(),
                         datetime.strptime(event['time'],'%H:%M').time(),
                         event['link']])
    return container