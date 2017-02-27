from Venues.Paradiso import ParadisoLoader
from Venues.Paard    import PaardLoader
from Venues.ZiggoDome import ZiggoDomeLoader

#Call functions to parse the RSS feeds
paard_container     = PaardLoader('http://www.paard.nl/programme/rss/lang/nl')
#paradiso_container  = ParadisoLoader('https://www.paradiso.nl/rss.xml')
#ziggodome_container = ZiggoDomeLoader()

#print numbers
#print("Paard: %s, Paradiso: %s, ZiggoDome: %s" % (len(paard_container),  len(paradiso_container), len(ziggodome_container)))

print(paard_container)

print ', '.join(paard_container)