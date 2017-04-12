from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests

def ArenaLoader():
    locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch

    URL = 'http://www.amsterdamarena.nl/kalender.htm'
    container = []
    
    #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").findAll('table'):
        date_first = link.find('thead').find('td').text
        
        event_list = link.find('tbody').findAll('tr')
        for event in event_list:
            title = event.find('a').text
            if 'Ajax' not in title and 'Nederland' not in title:
                url      = 'http://www.amsterdamarena.nl' + event.find('a')['href']
                raw_date = event.find('div',attrs={'class':'date-box'}).find('strong').text + ' '+ date_first
            
                date = datetime.strptime(raw_date,'%d %B %Y').date()
                time = None
            
                container.append([title,
                              date,
                              time,
                              url])

    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US

    return container