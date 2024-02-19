from chronossus.chronossus import Chronossus

chron = Chronossus()
chron.init_objectives()
chron.place_action_tiles()
chron.init_action_board()
chron.init_chronology()
chron.save_chronossus_data()

    #ap.set_stage(1)
    #for i in range(6):
    #    print(ap.stages)
    #    print(ap.action)
    #    ap.leap()
