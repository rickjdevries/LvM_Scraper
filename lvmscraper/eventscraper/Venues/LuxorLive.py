from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests

def LuxorLiveLoader():
    try: #Rick
        locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
    except: #Sander
        locale.setlocale(locale.LC_ALL,'Dutch_Netherlands.1252')#Dutch

    URL = 'https://www.luxorlive.nl/agenda/'
    container = []
   
    #Scrape the main site for links to events
    for link in BeautifulSoup(requests.get(URL).content,"html.parser").findAll('div',attrs={'class':'item horizontal '}):
        title    = link.find('h3').text
        url      = link.find('a')['href']
        raw_date = link.find('meta',attrs={'itemprop':'startDate'})['content'].split('+')
        
        date_time = datetime.strptime(raw_date[0] + '+' + raw_date[-1].replace(':',''),'%Y-%m-%dT%H:%M:%S%z')
        date     = date_time.date()
        time     = date_time.time()

        # for entry in link.find('ul').findAll('li'):
            # if 'start' in str(entry):
                # time = datetime.strptime(str(entry).split('start ',1)[1][:5],'%H:%M').time()
        
        container.append([title,
                          date,
                          time,
                          url])
        
    try: #Rick
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
    except: #Sander
        locale.setlocale(locale.LC_ALL,'English_United States.1252')#English US
    return container