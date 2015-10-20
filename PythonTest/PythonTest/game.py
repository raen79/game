from items import *
from vendors import *
from monsters import *
from map import *
from player_character import *



stage1 = {"first room":td_room_01_001,
          "td_Room 02":td_room_01_002,
          "td_Room 03":td_room_01_003,
          "td_Room 04":td_room_01_004,
          "td_Room 05":td_room_01_005,
          "td_Room 06":td_room_01_006,
          "td_Room 08":td_room_01_008,         
          "td_Room 10":td_room_01_010,
          "td_Room 11":td_room_01_011,
          "td_Room 12":td_room_01_012,
          "td_Room 13":td_room_01_013,
          "td_Room 14":td_room_01_014,
          "td_Room 15":td_room_01_015,
          "td_Room 16":td_room_01_016,
          "td_Room 17":td_room_01_017,
          "td_Room 18":td_room_01_018,
          "td_Room 19":td_room_01_019,
          "td_Room 20":td_room_01_020
          }

stage2 = {"first room":rb_room_01_001,#Link to Tutorial
          "rb_Room 02":rb_room_01_002,
          "rb_Room 03":rb_room_01_003,
          "rb_Room 04":rb_room_01_004,
          "rb_Room 05":rb_room_01_005,
          "rb_Room 06":rb_room_01_006,#Items
          "rb_Room 07":rb_room_01_007,#Items
          "rb_Room 08":rb_room_01_008,#Items
          "rb_Room 09":rb_room_01_009,#Items
          "rb_Room 10":rb_room_01_010,#Items
          "rb_Room 11":rb_room_01_011,#Items
          "rb_Room 12":rb_room_01_012,
          "rb_Room 13":rb_room_01_013,
          "rb_Room 14":rb_room_01_014,
          "rb_Room 15":rb_room_01_015,
          "rb_Room 16":rb_room_01_016,
          "rb_Room 17":rb_room_01_017,#Health Potion, Vendor
          "rb_Room 18":rb_room_01_018,
          "rb_Room 19":rb_room_01_019,#Map
          "rb_Room 20":rb_room_01_020,#Link to Dungeon, Wolf
          "rb_Room 21":rb_room_01_021,#Items
          "rb_Room 22":rb_room_01_022,#Link to Dungeon
          "rb_Room 23":rb_room_01_023,#Vendor
          "rb_Room 24":rb_room_01_024,
          "rb_Room 25":rb_room_01_025,
          "rb_Room 26":rb_room_01_026,
          "rb_Room 27":rb_room_01_027,#Items
          "rb_Room 28":rb_room_01_028,#Items
          "rb_Room 29":rb_room_01_029,#Items
          "rb_Room 30":rb_room_01_030,
          "rb_Room 31":rb_room_01_031,#Stage Complete
          "rb_Room 32":rb_room_01_032,
          "rb_Room 33":rb_room_01_033,
          "rb_Room 34":rb_room_01_034,
          "rb_Room 35":rb_room_01_035,
          "rb_Room 36":rb_room_01_036,
          "pc_Room 01":pc_room_01_001,
          "pc_Room 02":pc_room_01_002,
          "pc_Room 03":pc_room_01_003,
          "pc_Room 04":pc_room_01_004,
          "pc_Room 05":pc_room_01_005,
          "pc_Room 06":pc_room_01_006,
          "pc_Room 07":pc_room_01_007,
          "pc_Room 08":pc_room_01_008,
          "pc_Room 09":pc_room_01_009,
          "pc_Room 10":pc_room_01_010
          }



dh_Game = {"name":"Dungeons & Dictionaries.",
        "description":"",
        "stages":{"Stage 1":stage1,
                  "Stage 2":stage2,
                  },
        "start_stage":"Stage 1",
        "start_room":"first room"
        }