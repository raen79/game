#forcechange
#Items _________________________________________



# Weapons
dh_sword_001 = {
"name":"Demo Sword",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"Property of group 02",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":3,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":3,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":7,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":1,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":["You swing your sword quickly"],"heavy attack":["You draw back your sword and thrust it forward with all your might"],"parry":["Bringing up your sword, you ready yourself an incoming attack"],"dodge":["You ready yourself to evade an oncoming blow"],"inaction":[""]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":1,                                                                 # How much you can sell the item for.
"buy_value":3,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"weapon",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""                                                            # When the item is used, the description that is printed (healing)
}

dh_sword_002 = {
"name":"Old Sword",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A sword that has past it's prime but still has some good swings left in it.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":3,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":3,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":10,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":1,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":["You swing your sword quickly"],"heavy attack":["You draw back your sword and thrust it forward with all your might"],"parry":["Bringing up your sword, you ready yourself an incoming attack"],"dodge":["You ready yourself to evade an oncoming blow"],"inaction":[""]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":1,                                                                 # How much you can sell the item for.
"buy_value":5,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"weapon",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""                                                            # When the item is used, the description that is printed (healing)
}

#Monster Weapons
dh_goblin_dagger_001 = {
"name":"Goblins dagger",
"description":"",
"stat_dict":{"STR":0,"DEX":3,"INT":0,"CON":0,},
"min_dmg":2,
"max_dmg":4,
"armour value":0,
"STR_req":0,
"mass":0.5,
"animations":{"light attack":["The goblin scurrys towards you, dagger ready."],"heavy attack":["The goblin charges towards you, screaming 'Die!'"],"parry":["The goblin looks at you, ready to strike back"],"dodge":["Light on it's feet, the goblin readys itself"],"inaction":[""]},
"sell_value":1,
"buy_value":3,
"hidden":False,
"heal_value":0,
"item_type":"weapon",
"use_description":""
}

dh_orc_club_001 = {
"name":"Orc Club",
"description":"",
"stat_dict":{"STR":4,"DEX":0,"INT":0,"CON":0,},
"min_dmg":3,
"max_dmg":7,
"armour value":0,
"STR_req":0,
"mass":0.5,
"animations":{"light attack":["The orc flails his club towards you."],"heavy attack":["Raising the club above his head, the orc slams it downward","Charging at you, the orc pulls his club back and swing violently."],"parry":["The orc brushes from side to side with his club"],"dodge":["The orc fumbles around and takes an odd line towards you"],"inaction":[""]},
"sell_value":1,
"buy_value":3,
"hidden":False,
"heal_value":0,
"item_type":"weapon",
"use_description":""
}

#Armour
dh_leather_armour_001 = {
"name":"Leather Armour",
"description":"Not the best armour you've seen but you'll take it over wearing cloth",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":2,
"STR_req":3,
"mass":1,
"animations":{},
"sell_value":0,
"buy_value":1,
"hidden":False,
"heal_value":0,
"item_type":"armour",
"use_description":""
}

dh_fine_leather_001 = {
"name":"Fine Leather Armour",
"description":"An improvement on most leather armour you've seen, the craftmanship and the ualtiy of the leather is very high.",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":4,
"STR_req":4,
"mass":1.5,
"animations":{},
"sell_value":2,
"buy_value":5,
"hidden":False,
"heal_value":0,
"item_type":"armour",
"use_description":""
}

#Monster Armour
dh_goblin_armour_001 = {
"name":"Goblin rags",
"description":"",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":1,
"STR_req":1,
"mass":0.5,
"animations":{},
"sell_value":0,
"buy_value":1,
"hidden":False,
"heal_value":0,
"item_type":"armour",
"use_description":""
}

dh_orc_skin_001 = {
"name":"Thick orc skin",
"description":"",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":2,
"STR_req":1,
"mass":0.5,
"animations":{},
"sell_value":0,
"buy_value":0,
"hidden":False,
"heal_value":0,
"item_type":"armour",
"use_description":""
}

#Consumables
dh_healing_001 = {
"name":"light healing potion",
"description":"",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":0,
"STR_req":0,
"mass":0.5,
"animations":{},
"sell_value":2,
"buy_value":10,
"hidden":False,
"heal_value":3,
"item_type":"healing",
"use_description":"You drink the potion and feel slightly refreshed."}

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
"animations":{"light attack":[""],"heavy attack":[""],"parry":[""],"dodge":[""]},
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
"animations":{"light attack":[""],"heavy attack":[""],"parry":[""],"dodge":[""]},
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
"animations":{"light attack":[""],"heavy attack":[""],"parry":[""],"dodge":[""]},
"sell_value":0,
"buy_value":0,
"hidden":True,
"heal_value":0,
"item_type":"",
"use_description":""
}



end_game_token = {
"name":"end game token",
"description":"",
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},
"min_dmg":0,
"max_dmg":0,
"armour value":0,
"STR_req":0,
"mass":0,
"animations":{"light attack":[""],"heavy attack":[""],"parry":[""],"dodge":[""]},
"sell_value":0,
"buy_value":0,
"hidden":True,
"heal_value":0,
"item_type":"",
"use_description":""
}