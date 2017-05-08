from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests, re

def TivoliLoader():
    base      = 'https://www.tivolivredenburg.nl/nl/?offset='
    genres    = ['pop','jazz']
    container = []
    
    for genre in genres:
        counter = 0
        while True:
            URL  = base + str(counter) + '&category=' + genre + '&viewmode=list'
            page = BeautifulSoup(requests.get(URL).content,"html.parser").findAll('article',attrs={'class':'event '})

            if page:
                counter += 1
                #Scrape the main site for links to events
                for link in page:
                    if link:
                        raw_datetime = link.find('time')['datetime'][:-6]
                        date_time  = datetime.strptime(raw_datetime,'%Y-%m-%dT%H:%M:%S')
                        date  = date_time.date()
                        time  = date_time.time()     
                        url   = 'https://www.tivolivredenburg.nl/' + link.find('a')['href']
                        title = link.find('a')['title']

                        container.append([title,date,time,url])
            else:
                break
    return container