previous_room = {}
current_room = {}
current_stage = {}

player = {
"name":"Matt",                                                                                      # Player's name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":3,"DEX":3,"INT":3,"CON":5},                                                 # the stats of the player
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":15,                                                                             # Current health of the player.
"max_health":15,                                                                                 # This will be calculated and updated based on the player's constitution.
"base_health":75,																				# This value is added to the usual health calculation of CON * 5
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      
"exp":0,                                                                                        
"inventory":[],                                                                                  # A list of item dictionaries representing the player's inventory  
"max_carry":0,
"gold":5,
"animations":{"light attack":[""],"heavy attack":[""],"parry":[""],"dodge":[""]}                        #the default animations for when the play does not have a weapon equipped
}