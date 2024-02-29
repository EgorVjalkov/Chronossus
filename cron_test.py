from chronossus.classes.chronossus import Chronossus
from chronossus.classes.chronology import Track

chron = Chronossus(expansions=['PIONEERS OF NEW EARTH'])
chron.init_chronology_track()
chron.chronology_track.go_for_(4)
i = chron.chronology_track.data
print(i)

    #ap.set_stage(1)
    #for i in range(6):
    #    print(ap.stages)
    #    print(ap.action)
    #    ap.leap()
