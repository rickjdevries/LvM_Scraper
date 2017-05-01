from datetime import datetime
from bs4      import BeautifulSoup
import locale, requests

def CarreLoader():
    URL             = 'https://carre.nl/en/calendar'
    event_base_url  = 'https://carre.nl'
    container       = []
    
    match_strings = ['row agendaitem ','row agendaitem inithidden ']

    for match_string in match_strings:
        #Scrape the main site for links to events
        for link in BeautifulSoup(requests.get(URL).content,"html.parser").findAll('div',attrs={'class':match_string}):
            title    = link.find('h2').text

            page_url = event_base_url + link.find('div',attrs={'class':'large-3 columns hide-for-small'}).find('a')['href']
            #Go to the event page to find the time
            page     = BeautifulSoup(requests.get(page_url).content,"html.parser")
            
            for event in page.find('section',attrs={'class':'active'}).findAll('tr'):
                raw_time = event.find('td',attrs={'class':'tijd'}).text
                raw_date = event.find('td',attrs={'class':'datum'}).text

                #Parse time and date
                try:
                    date_time = datetime.strptime(raw_date + ' ' + raw_time.replace(' h',''),'%a  %d %B %Y %H:%M')
                except:
                    locale.setlocale(locale.LC_ALL,'nl_NL.UTF-8')#Dutch
                    date_time = datetime.strptime(raw_date + ' ' + raw_time.replace(' uur',''),'%a  %d %B %Y %H:%M')
                    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')#English US
                
                container.append([title,
                              date_time.date(),
                              date_time.time(),
                              page_url])
    
    return container
