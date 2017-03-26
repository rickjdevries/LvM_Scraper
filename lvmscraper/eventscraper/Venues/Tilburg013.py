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
        #Compose the hyperlinks
        url = 'http://www.013.nl' + link['href']
                
        title     = link.find('span',attrs={'class':'event__act'}).text
        date_raw  = link.find('span',attrs={'class':'event__date'}).text.replace("'", "")
        time_raw  = link.find('div',attrs={'class':'event__meta'}).text.strip()[8:13]

        date_time  = datetime.strptime(date_raw + ' ' + time_raw,'%a  %d %b %y %H:%M')
        date = date_time.date()
        time = date_time.time()
        
        container.append([title,date,time,url])      
                          
    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
        
    return container