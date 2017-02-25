from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests

def BoerderijLoader():
    base_URL = 'http://cultuurpodiumboerderij.nl/programma/page/'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '}  
    container = []
    
    page_counter = 1
    go_on = True
    while go_on:
        URL = base_URL+str(page_counter)
        page = BeautifulSoup(requests.get(URL, headers=headers).content,"html.parser").findAll('div',attrs={'class':'event__archive__item'})
        if page:
            for event in page:
                eventURL = event.find('a')['href']
                eventPage = BeautifulSoup(requests.get(eventURL, headers=headers).content,"html.parser")
                
                date = event.find('time')['datetime']
                time = eventPage.find('div',attrs={'class':'event__details'}).findAll('ul')[1].findAll('li')[1].text.replace('Aanvang:','')

                try:
                    date_time  = datetime.strptime(date+time,'%Y-%m-%d %H:%M')
                except:
                    date_time  = datetime.strptime(date+time,'%Y-%m-%d %H.%M')
                
                container.append([event.find('a').text.strip(),
                                  date_time.date(),
                                  date_time.time(),
                                  eventURL]
                )
            page_counter += 1
        else:
            go_on = False
    return container