


#Items _________________________________________



# Weaopons
sword_001 = {
"name":"",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":[""],"Heavy attack":[""],"Parry":[""],"Dodge":[""]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":0,                                                                 # How much you can sell the item for.
"buy_value":0,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""                                                            # When the item is used, the description that is printed (healing)
}

#Class Trackers
class_fighter = {
"name":"fighter path",
"description":"",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":0,
"STR_req":0,
"mass":0,
"animations":{"light attack":[""],"Heavy attack":[""],"Parry":[""],"Dodge":[""]},
"sell_value":0,
"buy_value":0,
"hidden":True,
"heal_value":0,
"item_type":"",
"use_description":""
}

class_rogue = {
"name":"rogue path",
"description":"",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":0,
"STR_req":0,
"mass":0,
"animations":{"light attack":[""],"Heavy attack":[""],"Parry":[""],"Dodge":[""]},
"sell_value":0,
"buy_value":0,
"hidden":True,
"heal_value":0,
"item_type":"",
"use_description":""
}

class_mage = {
"name":"mage path",
"description":"",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":0,
"STR_req":0,
"mass":0,
"animations":{"light attack":[""],"Heavy attack":[""],"Parry":[""],"Dodge":[""]},
"sell_value":0,
"buy_value":0,
"hidden":True,
"heal_value":0,
"item_type":"",
"use_description":""
}




#Vendors ________________________________________

vendor_001 ={
    "name":"",                  # Name displayed for the vendor
    "description":"",           # Description printed for the vendor
    "stock_items":[],           # (List of item dictionary variables) e.g. [sword_001] Items the vendor has for sale 
    "acquired_items":[]         # (List of item dictionary variables) e.g. [sword_001] Items the player sells are stored here, they are still re-purchasable but only upon asking to view them to keep the shopping menu tidy. (Do not place items in here)
    }
    

# Monsters _______________________________________

goblin_001 = {
"name":"",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0},                                                 # the stats of the monster
"combat_dict":{"light attack":24,"Heavy attack":49,"Parry":74,"Dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":0,                                                                              # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":0,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4",75:sword_001}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}



# ROOMS _________________________________________

# Stage 1 Rooms
room_01_001 = {"name":"",                   # Name displayed on menus and while in the room
               "description":"",            # Main description displayed within a room
               "items":[],              # (List of item dictionary variables e.g. "item_list":sword_001,church_key001) Items "on the floor" of the room to be picked up or that have been dropped by the player 
               "item_auto_list":[],         # (List of item dictionary variables) e.g. [Sword_001] Items that will be automatically added to the player's inventory as long as the player does not currently have an item with the same NAME in their inventory. (NAME is the value within the "name" slot of the item dictionary) 
               "item_auto_take_list":[],    # (List of string item names) e.g. ["Sword"] Items that will be automatically removed from the player's inventory as long as the player has one. This will be ba based on the NAME of the item. (NAME is the value within the "name" slot of the item dictionary) 
               "exits":{},                  # Dictionary containing a command( this is now more flexibile and can be "OPEN DOOR" instead of "south") and the room key found in the current stages "rooms" dictionary. e.g "OPEN DOOR":"Room 15". Do not use long commands and do not use commands that could be generated by in room items "TAKE SWORD") 
               "exit_req_inv":{},           # Dictionary that contains matching keys to the room's exits. The value is a list containing the "name" values of items that must be in the player's inventory. E.g {"OPEN DOOR":["Church key"]}
               "exit_req_equ":{},           # Dictionary that contains matching keys to the room's exits. The value is a list containing the "name" values of items that must be equiped by the player. E.g {"CHARGE GOBLINS":["Dagger"]}
               "exit_req_stat":{},          # Dictionary that contains matching keys to the room's exits. The value contains a 3 character stat code and a minimum value seperated by a comma. The player must have at least that value in that stat to see the corresponding exit in their menu. E.g {"SMASH LOCK":"STR,25"}
               "exit_action_desc":{},       # Dictionary that contains matching keys to the room's exits. The value contains a description to be paired with short action words for the exit option. If a key from "exits" is not present in this dictionary a further description won't be offered in the menu E.g {"OPEN DOOR":" to open the door and head in to the church."}
                                            # Menu example: (in the below example "HEAD BACK" had no entry in "exit_action_desc" but "CONTINUE FORWARD" did)
                                            # Actions:
                                            # HEAD BACK
                                            # CONTINUE FORWARD to head down the cliff using the narrow path                                       
               "vendor":[],                 # The vendor dictionary present in the room. Leave as an empty dictionary for no vendor. 
               "monster_list":[],           # List containing monster dictionary variables for the room. If the list contains a monster , entering the room will start an encounter loop before the engine enters the room menu loop.
               "enter_encounter_desc":"",   # A short description to be displayed as an encounter starts in the room. Leave as an Empty string for no descrption. 
               "leave_encounter_desc":"",   # A short description to be displayed as an encounter ends in the room. Leave as an Empty string for no descrption.         
               "go_to_stage":""             # The engine will check this field first when a player enters the room, if not empty it will consult the game dictionary's "stages" field and move the player to the first room of that stage. 
               }

room_01_002 = {
                "name":"",
               "description":"",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

room_01_003 = {
                "name":"",
               "description":"",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }


# Add more rooms as needed


# Stage 2 Rooms
room_02_001 = {
                "name":"",
               "description":"",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":[],
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":[],
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

room_02_002 = {
               "name":"",
               "description":"",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":[],
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":[],
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

room_02_003 = {
               "name":"",
               "description":"",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":[],
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":[],
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }


# Add more rooms as needed


# STAGES _________________________________________
stage1 = {"Room 1":room_01_001,
          "Room 2":room_01_002,
          "Room 3":room_01_003
          }

stage2 = {"Room 1":room_02_001,
          "Room 2":room_02_002,
          "Room 3":room_02_003
          }

stage3 = {}

stage4 = {}



# GAME ____________________________________________
Game = {"name":"",
        "description":"",
        "stages":{"Stage1":stage1,
                  "Stage2":stage2,
                  "Stage3":stage3,
                  "Stage4":stage4,}
        }