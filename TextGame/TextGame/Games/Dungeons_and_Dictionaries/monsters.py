# Monsters _______________________________________
from .items import *

goblin_warrior_001 = {
"name":"Goblin Warrior",                                                                                      # Name displayed in combat 
"description":"Carrying a sword half it's size and clad in makeshift armour, this goblin is all offense.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{29:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_sword_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":50,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 5"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}


goblin_warrior_002 = {
"name":"Goblin Warrior",                                                                                      # Name displayed in combat 
"description":"Carrying a sword half it's size and clad in makeshift armour, this goblin is all offense.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{29:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_sword_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":50,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 5"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

goblin_warrior_003 = {
"name":"Goblin Warrior",                                                                                      # Name displayed in combat 
"description":"Carrying a sword half it's size and clad in makeshift armour, this goblin is all offense.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{29:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_sword_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":50,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 5"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

goblin_thief_001 = {
"name":"Goblin Thief",                                                                                      # Name displayed in combat 
"description":"Wearing all black, this goblin thinks he's looking pretty cool.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":1,"INT":0,"CON":9,},                                                 # the stats of the monster
"combat_dict":{59:"light attack",69:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_dagger_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":45,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":45,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 4"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

goblin_thief_002 = {
"name":"Goblin Thief",                                                                                      # Name displayed in combat 
"description":"Wearing all black, this goblin thinks he's looking pretty cool.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":1,"INT":0,"CON":9,},                                                 # the stats of the monster
"combat_dict":{59:"light attack",69:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_dagger_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":45,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":45,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 4"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

orc_001 = {
"name":"Orc",                                                                                      # Name displayed in combat 
"description":"Towering over the goblins, these guys are in charge! Watch out for their heavy attacks.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":12,},                                                 # the stats of the monster
"combat_dict":{29:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":TB_orc_armour_001,                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_orc_club_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":60,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":60,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 10"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

orc_002 = {
"name":"Orc",                                                                                      # Name displayed in combat 
"description":"Towering over the goblins, these guys are in charge! Watch out for their heavy attacks.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":12,},                                                 # the stats of the monster
"combat_dict":{29:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":TB_orc_armour_001,                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_orc_club_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":60,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":60,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 10"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}
tutorial_orc_001 = {
"name":"Orc",                                                                                      # Name displayed in combat 
"description":"Obviously the raid leader, this Orc is hefting a club even bigger than you.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{29:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":TB_orc_armour_001,                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_orc_club_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":50,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

orc_chief_001 = {
"name":"Orc Chief",                                                                                      # Name displayed in combat 
"description":"The Orc Chief is huge, he must be part Troll!",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":18,},                                                 # the stats of the monster
"combat_dict":{19:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":TB_orc_armour_001,                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":Orc_cheif_Sword_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":90,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":90,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 15"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

giant_rat_001 = {
"name":"Giant Rat",                                                                                      # Name displayed in combat 
"description":"The size of a small dog, this rat is crazed and hungry!",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":9,},                                                 # the stats of the monster
"combat_dict":{49:"light attack",59:"heavy attack",69:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_giant_rat_claws_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":45,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":45,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 4"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

wolf_001 = {
"name":"Wolf",                                                                                      # Name displayed in combat 
"description":"Mangy and starving, this Wolf will attack anything that moves.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{59:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_wolf_teeth_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":50,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 6"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

wolf_002 = {
"name":"Wolf",                                                                                      # Name displayed in combat 
"description":"Mangy and starving, this Wolf will attack anything that moves.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{59:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_wolf_teeth_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":50,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 6"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

tutorial_goblin_fighters_001 = {
"name":"Goblin Fighter",                                                                                      # Name displayed in combat 
"description":"This goblin is bigger and burlier than it's peers. (Expect some Heavy Attacks!)",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":7,},                                                 # the stats of the monster
"combat_dict":{19:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_sword_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":35,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":35,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 2"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

tutorial_goblin_fighters_002 = {
"name":"Goblin Fighter",                                                                                      # Name displayed in combat 
"description":"This goblin is bigger and burlier than it's peers. (Expect some Heavy Attacks!)",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":7,},                                                 # the stats of the monster
"combat_dict":{19:"light attack",79:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_sword_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":35,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":35,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 2"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

tutorial_goblin_rogue_001 = {
"name":"Goblin Rogue",                                                                                      # Name displayed in combat 
"description":"These goblins are small and light on their feet. (This description implies that these Goblins will use light attacks, try Parry!)",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":6,},                                                 # the stats of the monster
"combat_dict":{39:"light attack",49:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_dagger_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":30,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":30,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 2"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

tutorial_goblin_rogue_002 = {
"name":"Goblin Rogue",                                                                                      # Name displayed in combat 
"description":"This goblin is small and light on his feet. (This description implies that these Goblins will use light attacks, try Parry!)",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":6,},                                                 # the stats of the monster
"combat_dict":{39:"light attack",49:"heavy attack",89:"parry",99:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_dagger_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":30,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":30,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 2"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

tutorial_goblin_mage_001 = {
"name":"Goblin Mage",                                                                                      # Name displayed in combat 
"description":"This goblin has learnt some spells it shouldn't have. Seems more likely to blow himself up.",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":8,},                                                 # the stats of the monster
"combat_dict":{19:"light attack",39:"heavy attack",49:"parry",59:"dodge"},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":TB_Goblin_staff_001,                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":40,                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":40,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"}, {70:"GOLD x 2"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}