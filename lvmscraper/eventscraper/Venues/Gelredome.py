from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests

def GelredomeLoader():
    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch

    URL = 'http://www.gelredome.nl/nl/evenementen'
    container = []
   
    # #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").findAll('div',attrs={'class':'agenda-items__content '}):       
        title    = link.find('h3').text
        if 'Vitesse' not in title:
            url      = 'http://www.gelredome.nl' + link.find('a')['href']
            
            day   = link.find('div',attrs={'class':'agenda-items__day'}).text.strip()
            month = link.find('div',attrs={'class':'agenda-items__month'}).text.strip()
            date  = datetime.strptime(day + ' ' + month,'%d %B %Y').date()
            time  = None

            container.append([title,
                              date,
                              time,
                              url])
        
    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
    return container