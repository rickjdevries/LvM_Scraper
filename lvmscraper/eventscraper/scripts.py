from .models               import Event
import eventscraper.Venues as     venues
import pandas              as     pd
import math

def import_file(f):   
    #Import the file with pandas
    df = pd.read_csv(f, encoding = "ISO-8859-1")

    #loop over the rows and store them in an object
    for index, row in df.iterrows():
        if type(row.Time) is str:
            Event.objects.get_or_create(
                venue = row.Venue,
                title = row.Title,
                date  = row.Date,
                time  = row.Time,
                URL   = row.URL
            )
        else:
            Event.objects.get_or_create(
                venue = row.Venue,
                title = row.Title,
                date  = row.Date,
                URL   = row.URL
        )
        
def scrape_events():
    #Call functions to parse the RSS feeds
    Boerderij_container  = venues.BoerderijLoader()
    AFAS_container       = venues.AFASLiveLoader()
    paard_container      = venues.PaardLoader()
    paradiso_container   = venues.ParadisoLoader()
    ziggodome_container  = venues.ZiggoDomeLoader()
    Tilburg013_container = venues.Tilburg013Loader()
    melkweg_container    = venues.MelkwegLoader()
    arena_container      = venues.ArenaLoader()
    luxorlive_container  = venues.LuxorLiveLoader()
    gelredome_container  = venues.GelredomeLoader()
    steck_container      = venues.SteckLoader()
    
    Venues = [[Boerderij_container,'Boerderij'],[AFAS_container,'AFAS Live'],[paard_container,'Paard'],[paradiso_container,'Paradiso'],[ziggodome_container,'Ziggo Dome'],[Tilburg013_container,' Tilburg 013'],[melkweg_container,'Melkweg'],[arena_container,'Arena'],[luxorlive_container,'Luxor Live'],[gelredome_container,'Gelredome'],[steck_container,'STECK']]

    for venue in Venues:
        #Loop over the entries
        for entry in venue[0]:
            Event.objects.get_or_create(
                venue = venue[1],
                title = entry[0],
                date  = entry[1],
                time  = entry[2],
                URL   = entry[3]
            )