from Venues.Paradiso  import ParadisoLoader
from Venues.Paard     import PaardLoader
from Venues.ZiggoDome import ZiggoDomeLoader
from Venues.AFASLive  import AFASLiveLoader

#Call functions to parse the RSS feeds
AFAS_container      = AFASLiveLoader()
paard_container     = PaardLoader()
paradiso_container  = ParadisoLoader()
ziggodome_container = ZiggoDomeLoader()

#print numbers
print(len(AFAS_container),len(paard_container),len(paradiso_container),len(ziggodome_container))