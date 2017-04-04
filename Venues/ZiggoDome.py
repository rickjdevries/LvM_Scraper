from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests, re

def ZiggoDomeLoader():
    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch

    URL = 'https://www.ziggodome.nl/agenda'
    container = []
   
    #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").find('div',attrs={'class':'agenda_overview '}).findAll('a',href=True):
        #Abstract some information
        # event_status = link.find('span',attrs={'class':'event_status'}).text
        # genre        = link.find('span',attrs={'class':'genre'}).text

        url = link['href']
        #open the event page
        event_data = BeautifulSoup(requests.get(url).content,"html.parser")
        
        raw_date  = event_data.find('div',attrs={'class':'titlebar'}).find('h2',attrs={'class':'event_date'}).text.strip()
        raw_time  = event_data.findAll('script',attrs={'id':'timetable'})       
        
        #Final data
        title     = event_data.find('h1',attrs={'class':'event_title'}).text
        date      = datetime.strptime(raw_date,'%A %d %B %Y').date()
        time      = None
        time_data = re.findall('<td>([a-zA-Z0-9.:&_ -]+)</td>',str(raw_time))
             
        if time_data:
            indices = [i for i, s in enumerate(time_data) if 'Start' in s or 'Aanvang' in s or title in s]
            if indices:
                time = datetime.strptime(time_data[max(indices)-1],'%H:%M').time()
                
        container.append([title,
                          date,
                          time,
                          url])

    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
    return container