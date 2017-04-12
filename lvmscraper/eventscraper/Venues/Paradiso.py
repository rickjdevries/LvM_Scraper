from datetime import datetime
from bs4      import BeautifulSoup
import ssl, locale, feedparser

def ParadisoLoader():
    URL = 'https://www.paradiso.nl/rss.xml'

    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
        
    feed = feedparser.parse(URL)
    container = []
    #Loop over the events

    locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch

    for event in feed['entries']:
        info       = event['title'].split(' - ')
        try:
            date_time  = datetime.strptime(info[0],'%A %d %B %Y %H:%M')
        except:
            date_time  = datetime.strptime(info[0]+' 00:00','%A %d %B %Y %H:%M')
        
        title = info[1]
        date  = date_time.date()
        time  = date_time.time()
        url   = event['link']
        
        container.append([title,date,time,url])
    
    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US

    return container