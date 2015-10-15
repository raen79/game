from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
Player_MaxCarryMass = 3.0
# Start game at the reception
current_room = rooms["Reception"]

def GetInventoryTotalMass():
    TotalMass = 0.0
    for item in inventory:
        TotalMass += item["mass"]
    return TotalMass
