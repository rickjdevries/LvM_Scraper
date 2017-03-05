from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests, re

def MelkwegLoader():
    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch

    URL = 'https://www.melkweg.nl/nl/agenda/'
    container = []
        
    #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").findAll('script',attrs={'type':'application/ld+json'}):
        #Apply regular expressions to abstract info from script tags
        title      = re.search('"name": "([a-zA-Z0-9.&_ -]+)"',str(link))
        datestring = re.search('"startDate" : "([a-zA-Z0-9.&:+_ -]+)"',str(link))
        url        = re.search('"url" : "([a-zA-Z0-9.:&/_ -]+)"',str(link))
        
        #If all data is found
        if title and datetime and url:
            date_time = datetime.strptime(datestring.groups()[0],'%Y-%m-%dT%H:%M:%S%z')
            
            container.append([title.groups()[0],
                                  date_time.date(),
                                  date_time.time(),
                                  url.groups()[0]])
    return container