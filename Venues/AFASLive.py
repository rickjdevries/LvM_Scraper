from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests

def AFASLiveLoader():
    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch
        
    URL = 'https://www.afaslive.nl/agenda'
    container = []
    
    for event in BeautifulSoup(requests.get(URL).content,"html.parser").findAll('figure',attrs={'data-bg-color':'#005FAA'}):
        title    = event.find('h3',attrs={'class':'eventTitle hide-for-small-only'}).text
        url      = event.find('a')['href']
        raw_date = event.find('time').text[2:]
        try:
            time      = event.find('div',attrs={'class':'times'}).find('span').text.replace(' uur','').strip()
            date_time = datetime.strptime(raw_date+' '+time,'%A %d %B %Y %H:%M')
            date      = date_time.date()
            time      = date_time.time()
            
        except:
            date = datetime.strptime(raw_date,'%A %d %B %Y')
            time = None

        container.append([title,
                          date,
                          time,
                          url]
        )
        
    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
    return container