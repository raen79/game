from items import *
from vendors import *
from monsters import *
from map import *



dh_stage1 = {"first room":dh_room_01_001,
          "Room 2":dh_room_01_002,
          "Room 3":dh_room_01_003,
          "Room 4":dh_room_01_004

          }

dh_stage2 = {"first room":dh_room_02_001
          }



dh_Game = {"name":"Demo Game",
        "description":"",
        "stages":{"Stage 1":dh_stage1,
                  "Stage 2":dh_stage2,
                  },
        "start_stage":"Stage 1",
        "start_room":"first room"
        }