from .items import *
from .vendors import *
from .monsters import *
from .map import *
from .player_character import *



stage1 = {"first room":td_room_01_001,
          "td_room 02":td_room_01_002,
          "td_room 03":td_room_01_003,
          "td_room 04":td_room_01_004,
          "td_room 05":td_room_01_005,
          "td_room 06":td_room_01_006,
          "td_room 08":td_room_01_008,         
          "td_room 10":td_room_01_010,
          "td_room 11":td_room_01_011,
          "td_room 12":td_room_01_012,
          "td_room 13":td_room_01_013,
          "td_room 14":td_room_01_014,
          "td_room 15":td_room_01_015,
          "td_room 16":td_room_01_016,
          "td_room 17":td_room_01_017,
          "td_room 18":td_room_01_018,
          "td_room 19":td_room_01_019,
          "td_room 20":td_room_01_020
          }

stage2 = {"first room":rb_room_01_001,#Link to Tutorial
          "rb_room 02":rb_room_01_002,
          "rb_room 03":rb_room_01_003,
          "rb_room 04":rb_room_01_004,
          "rb_room 05":rb_room_01_005,
          "rb_room 06":rb_room_01_006,#Items
          "rb_room 07":rb_room_01_007,#Items
          "rb_room 08":rb_room_01_008,#Items
          "rb_room 09":rb_room_01_009,#Items
          "rb_room 10":rb_room_01_010,#Items
          "rb_room 11":rb_room_01_011,#Items
          "rb_room 12":rb_room_01_012,
          "rb_room 13":rb_room_01_013,
          "rb_room 14":rb_room_01_014,
          "rb_room 15":rb_room_01_015,
          "rb_room 16":rb_room_01_016,
          "rb_room 17":rb_room_01_017,#Health Potion, Vendor
          "rb_room 18":rb_room_01_018,
          "rb_room 19":rb_room_01_019,#Map
          "rb_room 20":rb_room_01_020,#Link to Dungeon, Wolf
          "rb_room 21":rb_room_01_021,#Items
          "rb_room 22":rb_room_01_022,#Link to Dungeon
          "rb_room 23":rb_room_01_023,#Vendor
          "rb_room 24":rb_room_01_024,
          "rb_room 25":rb_room_01_025,
          "rb_room 26":rb_room_01_026,
          "rb_room 27":rb_room_01_027,#Items
          "rb_room 28":rb_room_01_028,#Items
          "rb_room 29":rb_room_01_029,#Items
          "rb_room 30":rb_room_01_030,
          "rb_room 31":rb_room_01_031,#Stage Complete
          "rb_room 32":rb_room_01_032,
          "rb_room 33":rb_room_01_033,
          "rb_room 34":rb_room_01_034,
          "rb_room 35":rb_room_01_035,
          "rb_room 36":rb_room_01_036,
          "pc_room 01":pc_room_01_001,
          "pc_room 02":pc_room_01_002,
          "pc_room 03":pc_room_01_003,
          "pc_room 04":pc_room_01_004,
          "pc_room 05":pc_room_01_005,
          "pc_room 06":pc_room_01_006,
          "pc_room 07":pc_room_01_007,
          "pc_room 08":pc_room_01_008,
          "pc_room 09":pc_room_01_009,
          "pc_room 10":pc_room_01_010
          }


game = {"name":"Dungeons & Dictionaries.",
        "description":"",
        "stages":{"Stage 1":stage1,
                  "Stage 2":stage2,
                  },
        "start_stage":"Stage 1",
        "start_room":"first room"
        }