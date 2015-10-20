# Monsters _______________________________________

goblin_warrior_001 = {
"name":"Goblin Warrior",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":9,"heavy attack":39,"parry":89,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{TB_Goblin_dagger_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}


goblin_warrior_002 = {
"name":"Goblin Warrior",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":1,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":9,"heavy attack":39,"parry":89,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{TB_Goblin_dagger_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

goblin_warrior_003 = {
"name":"Goblin Warrior",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":9,"heavy attack":39,"parry":89,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{TB_Goblin_dagger_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":50,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

goblin_thief_001 = {
"name":"Goblin Thief",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":1,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":9,"heavy attack":59,"parry":89,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{TB_Goblin_staff_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":60,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

goblin_thief_002 = {
"name":"Goblin Thief",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":1,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":9,"heavy attack":59,"parry":89,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{TB_Goblin_staff_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":60,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 2"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}
orc_001 = {
"name":"Orc",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":39,"heavy attack":49,"parry":59,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{TB_orc_armour_001},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{TB_orc_club_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":75,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 10"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

orc_002 = {
"name":"Orc",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":39,"heavy attack":49,"parry":59,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{TB_orc_armour_001},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{TB_orc_club_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":75,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 10"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

orc_chief_001 = {
"name":"Orc Chief",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":1,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":49,"heavy attack":69,"parry":79,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{TB_orc_armour_001},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{Orc_cheif_Sword_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":"85",                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 15"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}

giant_rat_001 = {
"name":"Giant Rat",                                                                                      # Name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":0,"DEX":1,"INT":0,"CON":10,},                                                 # the stats of the monster
"combat_dict":{"light attack":59,"heavy attack":79,"parry":89,"dodge":99},                      # the probability distribution for the actions of the monster. The engine will generate a number between 0 and 99 and the first number in this dictionary that the generated number is les or equal to is the action taken. remember 0-24 is 25 values i.e 25%
"combat_stat":"",                                                                               # The stat used for damage calculation. e.g. "STR"
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{TB_giant_rat_claws_001},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":"max_health",                                                                             # Current health of the monster. Set this to what you want the monster to begin on. (usualy equal to the max health value - rememeber the max health will be calculated by the engine at the begining of the counter)
"max_health":90,                                                                                 # This will be calculated and updated based on the monsters constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      # Used for generating an exp value for defeating this enemy. (try to make sure the stats make sense based on this level)
"loot":[{99:"GOLD x 15"},{70:"GOLD x 4"}]                                           # A list of dictionaries containing probability distribution for loot gained by killing the monster. The engine will look at each dictionary and roll a number between 0 and 99 for each one. Thus you can give multiple items from one monster.
                                                                                                #Gold drops should be entered as a string in the format "GOLD x #" where # is replaced with the amount gained.  
}