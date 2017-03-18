from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests, re

def SteckLoader():
    URL = 'http://www.steck.nl/#kalender'
    container = []
   
    #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").findAll('div',attrs={'class':'event Live'}):
        url        = 'http://www.steck.nl/' + link.find('a')['href']
        script     = link.find('script',attrs={'type':'application/ld+json'})
        title      = re.search('"name": "([a-zA-Z0-9.:,&+_ -]+)"',str(script)).groups()[0]
        datestring = re.search('"startDate" : "([a-zA-Z0-9.&:+_ -]+)"',str(link)).groups()[0]
        timestring = re.search('"doorTime" : "([a-zA-Z0-9.&:+_ -]+)"',str(link)).groups()[0]
        date_time  = datetime.strptime(datestring+' '+timestring,'%Y-%m-%d %H:%M:%S')
        date       = date_time.date()
        time       = date_time.time()
                
        container.append([title,
                          date,
                          time,
                          url])

    return container