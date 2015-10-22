#forcechange
from .items import *

dh_goblin_001 = {
"name":"Frenzied Goblin",                                                                                      
"description":"Snarling and ugly",                                                                               
"stat_dict":{"STR":3,"DEX":3,"INT":3,"CON":3},                                                 
"combat_dict":{64:"light attack",69:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"DEX",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":dh_goblin_armour_001,                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":dh_goblin_dagger_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":15,                                                                              # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":15,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4",75:dh_healing_001}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

dh_goblin_002 = {
"name":"Frenzied Goblin",                                                                                      
"description":"Snarling and ugly",                                                                               
"stat_dict":{"STR":3,"DEX":3,"INT":3,"CON":3},                                                 
"combat_dict":{64:"light attack",69:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"DEX",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":dh_goblin_armour_001,                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":dh_goblin_dagger_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":15,                                                                              # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":15,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4",75:dh_healing_001}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

dh_orc_001 = {
"name":"Orc Commander",                                                                                      
"description":"Both burlier and uglier than the goblins he leads, it is likely he earned his position by just being bigger!",                                                                               
"stat_dict":{"STR":8,"DEX":5,"INT":2,"CON":5},                                                 
"combat_dict":{19:"light attack",89:"heavy attack",94:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"STR",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":dh_orc_skin_001,                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":dh_orc_club_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":25,                                                                              # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":25,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":5,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4",75:dh_healing_001}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}