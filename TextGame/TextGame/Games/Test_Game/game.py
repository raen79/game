#forcechange
from .items import *
from .vendors import *
from .monsters import *
from .map import *
from .player_character import *



dh_stage1 = {"first room":dh_room_01_001,
          "Room 2":dh_room_01_002,
          "Room 3":dh_room_01_003,
          "Room 4":dh_room_01_004

          }

dh_stage2 = {"first room":dh_room_02_001
          }



game = {"name":"Test Game",
        "description":"Used for quick testing of engine features!" May be unstable!,
        "stages":{"Stage 1":dh_stage1,
                  "Stage 2":dh_stage2,
                  },
        "start_stage":"Stage 1",
        "start_room":"first room"
        }