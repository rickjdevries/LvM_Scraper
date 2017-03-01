from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests

def Tilburg013Loader():
    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch

    URL = 'http://www.013.nl/programma'
    container = []
   
    #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").find('div',attrs={'class':'event-overview'}).findAll('a',href=True):
        #Abstract some information
        #event_date = link.find('span',attrs={'class':'event_date'}).text
        #event_act = link.find('span',attrs={'class':'event_act'}).text

        url = link['href']
        #combine the hyperlinks
        url = 'http://www.013.nl' + url
        #print(url)
        
        ##open the event page
        event_data = BeautifulSoup(requests.get(url).content,"html.parser").find('div',attrs={'class':'spotlight'})
        
        title = event_data.find('h1',attrs={'class':'spotlight__title title--alpha'}).text
        date  = event_data.find('span',attrs={'class':'spotlight__date'}).text
        #date_time  = datetime.strptime(date.strip(),'%A %d %B %Y')
        
        container.append([title, date])          
                          
    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
        
    return container