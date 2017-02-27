from Venues.Paradiso  	import ParadisoLoader
from Venues.Paard    	import PaardLoader
from Venues.ZiggoDome 	import ZiggoDomeLoader
from Venues.AFASLive  	import AFASLiveLoader
from Venues.Boerderij   import BoerderijLoader
from Venues.Tilburg013	import Tilburg013Loader

#Call functions to parse the RSS feeds
#paard_container     = PaardLoader('http://www.paard.nl/programme/rss/lang/nl')
#paradiso_container  = ParadisoLoader('https://www.paradiso.nl/rss.xml')
#ziggodome_container = ZiggoDomeLoader()

#print numbers
#print("Paard: %s, Paradiso: %s, ZiggoDome: %s" % (len(paard_container),  len(paradiso_container), len(ziggodome_container)))

#print(paard_container)

#print ', '.join(paard_container)
#Boerderij_container = BoerderijLoader()
#AFAS_container      = AFASLiveLoader()
#paard_container     = PaardLoader()
#paradiso_container  = ParadisoLoader()
#ziggodome_container = ZiggoDomeLoader()
Tilburg013_container       = Tilburg013Loader()

#print numbers
#print(len(Boerderij_container),len(AFAS_container),len(paard_container),len(paradiso_container),len(ziggodome_container))
print(len(Tilburg013_container))