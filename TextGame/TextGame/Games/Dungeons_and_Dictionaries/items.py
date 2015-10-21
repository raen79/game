# Weaopons
item_001 = {
"name":"",                                                                      
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
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"",                                                                 
"use_description":""    }    

TB_bandages_001 = {
"name":"Bandages",                                                                      
"description":"Use these to help the Wounded Vendor.",                                                                
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                  
"min_dmg":0,                                                                    
"max_dmg":0,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":[""],"Heavy attack":[""],"Parry":[""],"Dodge":[""]},  
"sell_value":5,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"",                                                                 
"use_description":""    }                                                      

TB_Tutorial_sword_001 = {
"name":"Battered Sword",                                                                     
"description":"The sword is battered and has not been cleaned in a while.",                                                               
"stat_dict":{"STR":3,"DEX":0,"INT":0,"CON":0,},                                 
"min_dmg":5,                                                                   
"max_dmg":9,                                                                 
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":1,                                                                       
"animations":{"light attack":["You quickly thrust at your opponent,"],"heavy attack":["You bring you sword down with all your might"],"parry":["You get ready to deflect their attak,"],"dodge":["You jump to the side"]},  
"sell_value":3,                                                                 
"buy_value":10,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                 
"item_type":"weapon",                                                                  
"use_description":""    }  

TB_Tutorial_dagger_001 = {
"name":"Dagger",                                                                     
"description":"Orange from rust, it looks like it has a few more hits in it.",                                                               
"stat_dict":{"STR":0,"DEX":7,"INT":0,"CON":0,},                                 
"min_dmg":7,                                                                   
"max_dmg":8,                                                                 
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":1,                                                                       
"animations":{"light attack":["Like lighting you bring the blade to your foe,"],"heavy attack":["You gear up and then charge with the small blade,"],"parry":["You bring the blade close to your body, ready to fend off their attack,"],"dodge":["You pounce back,"]},  
"sell_value":0,                                                                 
"buy_value":10,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                 
"item_type":"weapon",                                                                  
"use_description":""    }   

TB_Tutorial_Staff_001 = {
"name":"Old Staff",                                                                     
"description":"Not much more than a glorified stick. Looks cool though.",                                                               
"stat_dict":{"STR":0,"DEX":0,"INT":3,"CON":0,},                                 
"min_dmg":5,                                                                   
"max_dmg":12,                                                                 
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":1,                                                                       
"animations":{"light attack":["You shoot out a quick fire ball"],"heavy attack":["You concentrate the ancient power within the staff, to realse a great flame,"],"parry":["You create a reflection shield"],"dodge":["Holding your staff close to your chest, you scamper around,"]},  
"sell_value":0,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                 
"item_type":"weapon",                                                                  
"use_description":""    }        

TB_Church_key_001 = {
"name":"The Church Key",                                                                      
"description":"A heavy iron key, you feel the authority radiating from it.",                   
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 
"min_dmg":0,                                                                    
"max_dmg":0,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":[""],"Heavy attack":[""],"Parry":[""],"Dodge":[""]},  
"sell_value":0,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"",                                                                 
"use_description":"The Key fits in the lock and unlocks the door."  }   

Warrior_class = {
"name":"Warrior Path",                                                          
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
"use_description":""}

Rouge_class = {
"name":"Rouge path",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":0,                                                                 # How much you can sell the item for.
"buy_value":0,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":True,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""}

Mage_class = {
"name":"Mage path",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":0,                                                                 # How much you can sell the item for.
"buy_value":0,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":True,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""}

TB_Tutorial_Armour_001= {
"name":"Clothes",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"These are your clothes, you know what they are.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":1,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":1,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":3,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"armour",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""}

TB_Leather_Armour_001 = {
"name":"Leather Armour",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The Leather is firm, yet is a bit tight in certain areas. :(",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":2,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":2,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":3,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":2,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":10,                                                                 # How much you can sell the item for.
"buy_value":12,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"armour",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""}

TB_old_Armour_001 = {
"name":"Old Armour",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A set of old armour, the smell might fend off some of the weaker monsters!",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":2,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":4,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":3,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":4,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":10,                                                                 # How much you can sell the item for.
"buy_value":12,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"armour",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""}

TB_novice_robes_001 = {
"name":"Novice Robes",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The robes are pretty dull, yet they have awesome sleeves! *swish*",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":2,"CON":2,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":1,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":3,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":2,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":10,                                                                 # How much you can sell the item for.
"buy_value":12,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"armour",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""}

TB_steel_armour_001 = {
"name":"Steel Armour",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"This armour will hold off all but the greastest of tin openers.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":3,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":6,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":5,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":5,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":20,                                                                 # How much you can sell the item for.
"buy_value":24,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"armour",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    }     

TB_Studded_leather_armour_001 = {
"name":"Studded Leather Armour",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"These spikes are awesome, is this how a hedgehog feels?",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":3,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":4,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":3,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":3,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":20,                                                                 # How much you can sell the item for.
"buy_value":24,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"armour",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    }                     

TB_apprentice_robes_001 = {
"name":"Apprentice Robes",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"This scarlet robe makes you feel more confident that you can take on the world.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":3,"CON":3,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":2,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":3,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":2,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":20,                                                                 # How much you can sell the item for.
"buy_value":24,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"armour",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    }         

TB_Den_key_001 = {
"name":"Have not entered Den",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":0,                                                                 # How much you can sell the item for.
"buy_value":0,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":True,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    } 

TB_Den_key_002 = {
"name":"Have entered Den",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":0,                                                                 # How much you can sell the item for.
"buy_value":0,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":True,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    }

TB_pot_001 = {
"name":"Healing Potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The warm flask gives off a red glow.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":10,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":50,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"The potion makes you feel great! Did you check the contents?"    }

TB_pot_002 = {
"name":"Healing Potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The warm flask gives off a red glow.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":10,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":50,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"The potion makes you feel great! Did you check the contents?" }

TB_pot_003 = {
"name":"Healing Potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The warm flask gives off a red glow.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":10,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":50,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"The potion makes you feel great! Did you check the contents?" }

TB_pot_004 = {
"name":"Healing Potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The warm flask gives off a red glow.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":10,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":50,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"The potion makes you feel great! Did you check the contents?" }

TB_pot_005 = {
"name":"Healing Potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The warm flask gives off a red glow.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":10,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":50,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"The potion makes you feel great! Did you check the contents?" }

TB_pot_006 = {
"name":"Healing Potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The warm flask gives off a red glow.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":10,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":50,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"The potion makes you feel great! Did you check the contents?" }

TB_great_pot_001 = {
"name":"Great Healing potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A large flask which smells delicous.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":20,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":75,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"That is some good potion."    } 

TB_great_pot_002 = {
"name":"Great Healing potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A large flask which smells delicous.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":20,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":75,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"That is some good potion."    }

TB_great_pot_003 = {
"name":"Great Healing potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A large flask which smells delicous.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":20,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":75,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"That is some good potion."    }

TB_great_pot_004 = {
"name":"Great Healing potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A large flask which smells delicous.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":20,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":75,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"That is some good potion."    } 

TB_great_pot_005 = {
"name":"Great Healing potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A large flask which smells delicous.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":20,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":75,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"That is some good potion."    }

TB_great_pot_006 = {
"name":"Great Healing potion",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A large flask which smells delicous.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":0,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":0,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":0,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":2,                                                                 # How much you can sell the item for.
"buy_value":20,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":75,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"healing",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":"That is some good potion."    }

TB_steel_sword_001 = {
"name":"Steel Sword",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A Normal Sword, recently sharpened.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":2,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":10,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":15,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":5,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":2,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":["You send out a quick stab,"],"heavy attack":["Taking two hands on the sword, you swing with all your might, "],"parry":["You raise your sword to take on their attack,"],"dodge":["You dash to the right,","You dash to the left,"]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":15,                                                                 # How much you can sell the item for.
"buy_value":18,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"weapon",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    } 

TB_steel_dagger_001 = {
"name":"Steel Dagger",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"A wicked dagger, it has all the right curves.",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":2,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":13,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":14,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":3,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":1,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":["Within a matter of microsecounds, you arm is extended with dagger in hand,"],"heavy attack":["You get into a stance, and then jump to attack,"],"parry":["Beliving that the enemy will attack you get ready to parry,"],"dodge":["You cartwhell around the place,"]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":15,                                                                 # How much you can sell the item for.
"buy_value":18,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"weapon",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    } 

TB_wooden_staff_001 = {
"name":"Wooden Staff",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"Now that you have this, no one shall pass!",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":2,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":5,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":20,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":3,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":2,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":["You send a quick lighting bolt,"],"heavy attack":["Taking a deep breath,then send forth a lighting storm,"],"parry":["You create a lighting shield around your body,"],"dodge":["Screw this, lets run around the room,"]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":15,                                                                 # How much you can sell the item for.
"buy_value":18,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"weapon",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    } 

TB_fine_sword_001 = {
"name":"Finely Crafted Sword",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The sword feels well balanced, almost an extenstion of your arm. An extension made of STEEL!",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":3,"DEX":0,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":24,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":28,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":6,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":3,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":["You swing your sword, air whistling,"],"heavy attack":["You raise your sword, then bring it smashing down,"],"parry":["You have your sword ready for their attack,"],"dodge":["You drop to one side,"]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":20,                                                                 # How much you can sell the item for.
"buy_value":30,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"weapon",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    } 

TB_fine_dagger_001 = {
"name":"Finely Crafted Dagger",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"The blade is light yet is extremly sharp. *OUCH!*",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":3,"INT":0,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":26,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":27,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":2,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":["You flash foward the blade,"],"heavy attack":["With extra effect, you swing the dagger,"],"parry":["With a strong knowledge of parring, your muscle memory springs into action,"],"dodge":["You preform a backflip,"]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":20,                                                                 # How much you can sell the item for.
"buy_value":30,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"weapon",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    } 

TB_fine_Staff_001 = {
"name":"White Staff",                                                                      # Name of the item diplayed in the menu and also the name checked for exit requirements.
"description":"I didn't have to die to get the white version?!",                                                               # Description displayed when examining the item using the "LOOK" action 
"stat_dict":{"STR":0,"DEX":0,"INT":3,"CON":0,},                                 # Dictionary containing the stat modifiers equiping the item provides (Weapons and armour) 
"min_dmg":15,                                                                    # The minimum damage generated within combat when item is equiped as weapon (Weapon)
"max_dmg":35,                                                                    # The maximum damage generated within combat when item is equiped as weapon (Weapon)
"armour value":0,                                                               # The damage reduction provided by the item when equiped as armour (Armour)
"STR_req":0,                                                                    # The strength stat minimum requirement for equiping the item as armour (Armour)
"mass":3,                                                                       # The weight of the item used when checking if the player can carry more items.
"animations":{"light attack":["You cast a powerful wind burst,"],"heavy attack":["Concentrating on your staff, you unleash a mini-whirwind,"],"parry":["You create a high-pressure wind current around you,"],"dodge":["Cursing, you stumble to the ground,"]}, # When a player uses the item as a weapon and selects one of the actions. A random string will be selected from the list contained in the actions dictionary entry. e.g {"light attack":["You swing your sword quickly","you send out a fast paced jab with your blade"]  
"sell_value":20,                                                                 # How much you can sell the item for.
"buy_value":30,                                                                  # How much it costs the player to buy the item. (approx. 3 x the sell value)
"hidden":False,                                                                 # If true the item can be int he player's inventory without being printed. (used for items designed to track progress or choices)
"heal_value":0,                                                                 # The value healed if the item is used for healing (healing) 
"item_type":"weapon",                                                                 # A string value from "weapon","armour","healing","" (empty string for items which can neither be used as a weapon, equiped as armour or consumed to provide healing
"use_description":""    } 

TB_Goblin_sword_001 = {
"name":"Goblin Sword",                                                                      
"description":"",                                                                
"stat_dict":{"STR":1,"DEX":0,"INT":0,"CON":0,},                                  
"min_dmg":2,                                                                    
"max_dmg":5,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0.5,                                                                       
"animations":{"light attack":["The Goblin rushes you."],"heavy attack":["The Goblin jumps at you with sword ready."],"parry":["The Goblin eyes are on your sword."],"dodge":["The Goblin jumps back."]},  
"sell_value":5,                                                                 
"buy_value":7,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"weapon",                                                                 
"use_description":""    }

TB_Goblin_dagger_001 = {
"name":"Goblin dagger",                                                                      
"description":"",                                                                
"stat_dict":{"STR":0,"DEX":1,"INT":0,"CON":0,},                                  
"min_dmg":3,                                                                    
"max_dmg":4,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0.5,                                                                       
"animations":{"light attack":["The Goblin darts towards you, with aim to stick their dagger in your side."],"heavy attack":["The Goblin takes a deep breath, then hurles towards you."],"parry":["The Goblin raises his dagger, but is makes no moves towards you."],"dodge":["The Goblin tries to get out of the way."]},  
"sell_value":5,                                                                 
"buy_value":7,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"weapon",                                                                 
"use_description":""    }

TB_Goblin_staff_001= {
"name":"Goblin Staff",                                                                      
"description":"",                                                                
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                  
"min_dmg":1,                                                                    
"max_dmg":6,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0.5,                                                                       
"animations":{"light attack":["The Goblin sends out a ball of black magic hurlting towards you."],"heavy attack":["The Goblin shakes his staff, creating a black cloud above you."],"parry":["The Goblin wraps himself in his black magic."],"dodge":["Squeling, the Goblin trips over his own feet to get out of the way."], "inaction":["The Goblin attempts to throw a ball of flame at you. It sputters out in his hand."]},  
"sell_value":5,                                                                 
"buy_value":7,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"weapon",                                                                 
"use_description":""    }

TB_orc_armour_001 = {
"name":"Orc Armour",                                                                      
"description":"",                                                                
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                  
"min_dmg":0,                                                                    
"max_dmg":0,                                                                    
"armour value":2,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":[""],"heavy attack":[""],"parry":[""],"dodge":[""]},  
"sell_value":0,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"armour",                                                                 
"use_description":""    }

TB_orc_club_001 = {
"name":"Orc Club",                                                                      
"description":"",                                                                
"stat_dict":{"STR":2,"DEX":0,"INT":0,"CON":0,},                                  
"min_dmg":7,                                                                    
"max_dmg":11,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":["The Orc brings his club to your head."],"heavy attack":["Flexing his muscles, the orc raises his club with aim to crush you."],"parry":["The orc plants his feet and urges you to hit him."],"dodge":["The orc starts to move around more."]},  
"sell_value":9,                                                                 
"buy_value":15,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"weapon",                                                                 
"use_description":""    }

TB_giant_rat_claws_001 = {
"name":"gaint rat claws",                                                                      
"description":"",                                                                
"stat_dict":{"STR":0,"DEX":2,"INT":0,"CON":0,},                                  
"min_dmg":8,                                                                    
"max_dmg":10,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":["The rat takes a quick swape at you."],"heavy attack":["The rat jumps at you, mouth open."],"parry":["The rat eyes snap to your weapon"],"dodge":["The rat patters about."]},  
"sell_value":0,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"weapon",                                                                 
"use_description":""    }

TB_victory_001 = {
"name":"end game token",                                                                      
"description":"you have won the game!",                                                                
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                  
"min_dmg":0,                                                                    
"max_dmg":0,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":[""],"Heavy attack":[""],"Parry":[""],"Dodge":[""]},  
"sell_value":0,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"",                                                                 
"use_description":""    } 

Dynamite = {
"name":"Dynamite",                                                                      
"description":"A stash of Dynamite, could blow up some large stuff with this. This makes you incredibly nervous.",                                                                
"stat_dict":{"STR":0,"DEX":0,"INT":0,"CON":0,},                                  
"min_dmg":0,                                                                    
"max_dmg":0,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":[""],"heavy attack":[""],"parry":[""],"dodge":[""]},  
"sell_value":0,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"",                                                                 
"use_description":""    }

Orc_cheif_Sword_001 = {
"name":"Orc_cheif_Sword",                                                                      
"description":"",                                                                
"stat_dict":{"STR":3,"DEX":0,"INT":0,"CON":0,},                                  
"min_dmg":15,                                                                    
"max_dmg":20,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":["The Cheif moves with impressive speed towards you, sword swinging."],"heavy attack":["The Cheif shouts at you whilst lifting his great sword about his head."],"parry":[" 'C'mon, Hit me!, HIT ME!'' "],"dodge":["The Cheif attempts to get out of reach of your attack."]},  
"sell_value":0,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"weapon",                                                                 
"use_description":""    }

TB_wolf_teeth_001 = {
"name":"Wolf Teeth",                                                                      
"description":"",                                                                
"stat_dict":{"STR":0,"DEX":2,"INT":0,"CON":0,},                                  
"min_dmg":5,                                                                    
"max_dmg":12,                                                                    
"armour value":0,                                                               
"STR_req":0,                                                                    
"mass":0,                                                                       
"animations":{"light attack":["The Wolf nips at your leg."],"heavy attack":["The Wolf pounces for your jugular."],"parry":["The Wolf's eyes draw to your weapon"],"dodge":["The Wolf attempts to leap away."]},  
"sell_value":0,                                                                 
"buy_value":0,                                                                  
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"weapon",                                                                 
"use_description":""    }

TB_elder_map_001 = {
"name":"Forest map",                                                                      
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
"hidden":False,                                                                 
"heal_value":0,                                                                  
"item_type":"",                                                                 
"use_description":""    }   
