previous_room = {}
current_room = {}
current_stage = {}

player = {
"name":"",                                                                                      # Player's name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":3,"DEX":3,"INT":3,"CON":5},                                                 # the stats of the player
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":15,                                                                             # Current health of the player.
"max_health":15,                                                                                 # This will be calculated and updated based on the player's constitution.
"base_health":75,
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      
"exp":0,                                                                                        
"inventory":[],                                                                                  # A list of item dictionaries representing the player's inventory  
"max_carry":0,
"gold":10
}