from datetime import datetime
from bs4      import BeautifulSoup
import ssl, locale, feedparser

def ParadisoLoader(URL):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
        
    feed = feedparser.parse(URL)
    container = []
    #Loop over the events

    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
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