from Venues.Paradiso  	import ParadisoLoader
from Venues.Paard    	import PaardLoader
from Venues.ZiggoDome 	import ZiggoDomeLoader
from Venues.AFASLive  	import AFASLiveLoader
from Venues.Boerderij   import BoerderijLoader
from Venues.Tilburg013	import Tilburg013Loader

#Call functions to parse the RSS feeds
Boerderij_container  = BoerderijLoader()
AFAS_container       = AFASLiveLoader()
paard_container      = PaardLoader()
paradiso_container   = ParadisoLoader()
ziggodome_container  = ZiggoDomeLoader()
Tilburg013_container = Tilburg013Loader()

#print numbers
print("Boerderij: %s, Paard: %s, Paradiso: %s, ZiggoDome: %s, 013: %s" % (len(Boerderij_container),len(paard_container), len(paradiso_container), len(ziggodome_container), len(Tilburg013_container)))