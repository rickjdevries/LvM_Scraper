from Venues.Paradiso  import ParadisoLoader
from Venues.Paard     import PaardLoader
from Venues.ZiggoDome import ZiggoDomeLoader
from Venues.AFASLive  import AFASLiveLoader
from Venues.Boerderij import BoerderijLoader

#Call functions to parse the RSS feeds
Boerderij_container = BoerderijLoader()
AFAS_container      = AFASLiveLoader()
paard_container     = PaardLoader()
paradiso_container  = ParadisoLoader()
ziggodome_container = ZiggoDomeLoader()

#print numbers
print(len(Boerderij_container),len(AFAS_container),len(paard_container),len(paradiso_container),len(ziggodome_container))