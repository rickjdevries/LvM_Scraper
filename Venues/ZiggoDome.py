from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests

def ZiggoDomeLoader():
    import locale
    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch

    URL = 'https://www.ziggodome.nl/agenda'
    container = []
   
    #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").find('div',attrs={'class':'agenda_overview '}).findAll('a',href=True):
        #Abstract some information
        event_status = link.find('span',attrs={'class':'event_status'}).text
        genre        = link.find('span',attrs={'class':'genre'}).text

        url = link['href']
        #open the event page
        event_data = BeautifulSoup(requests.get(url).content,"html.parser").find('div',attrs={'class':'titlebar'})
        
        date  = event_data.find('h2',attrs={'class':'event_date'}).text
        date_time  = datetime.strptime(date.strip(),'%A %d %B %Y')
        
        #TODO: Abstract starting time from event page

        container.append([event_data.find('h1',attrs={'class':'event_title'}).text,
                          date_time.date(),
                          'time',
                          url])

    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
    return container