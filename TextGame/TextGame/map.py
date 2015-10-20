from items import *
from vendors import *
from monsters import *

#Tutorial (Stage1)

td_room_01_001 = {
               "name":"Home", #
               "description":"*BANG!* Your eyes fly open. What was that?! The room is bathed is a flickering red glow. Is that screaming? Quickly, grab your clothes and head downstairs!",
               "items":[TB_Tutorial_Armour_001],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"downstairs":"td_room 02"},
               "exit_req_inv":{"downstairs":["Clothes"]},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{""},
               "vendor":[TB_wounded_vendor_001],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}

			
td_room_01_002 = {
               "name":"Front Door", #
               "description":"You reach your front door. With your clothes equipped, you can investigate the Village Green.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"upstairs":"first room","east":"td_room 03"},
               "exit_req_inv":{},
               "exit_req_equ":{"east":["Clothes"]},
               "exit_req_stat":{},
               "exit_action_desc":{"upstairs":"to head back upstairs.", "east":"to investigate the Village."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
td_room_01_003 = {
               "name":"Village Green", #
               "description":"The Village is ablaze! You can barely see through all the smoke and ash. A man lays on the ground in a pool of blood. You notice some bandages on the floor. (Pick them up and help him!)",
               "items":[TB_bandages_001],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"help":"td_room 04"},
               "exit_req_inv":{"help":["Bandages"]},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"help":"to help the man on the ground",},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
     		}

td_room_01_004 = {
               "name":"Wounded Vendor", #
               "description":"You kneel down to help him. He grabs you by the shirt and screams, 'RAIDERS!'. Glancing around, you can see small figures cavorting in the smoke. Clearly they are still around!",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"talk":"td_room 05"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"talk":"to find out more about the attack"},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
			
td_room_01_005 = {
               "name":"Wounded Vendor", #
               "description":"'GOBLINS! Goblins everywhere! One of the vile demonspawn got me. Here, I'll give you this dagger for the bandages you're carrying.' (Trade your Bandages for his Dagger.)",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"confirm":"td_room 06"},
               "exit_req_inv":{"confirm":["Dagger"]},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"confirm":"to confirm the trade."},
               "vendor":[TB_wounded_vendor_001],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
td_room_01_006 = {
               "name":"Wounded Vendor", #
               "description":"*THWACK* Blood sprays across your face. An arrow potrudes from the Vendors chest. You see a goblin archer cackling gleefully from the tavern roof. A wounded soldier is trying to get to him, equip your dagger so you can go help.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"attack":"td_room 08"},
               "exit_req_inv":{},
               "exit_req_equ":{"attack":["Dagger"]},
               "exit_req_stat":{},
               "exit_action_desc":{"attack":"to go help the wounded soldier"},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
td_room_01_008 = {
               "name":"Village Green", #
               "description":"You look around the Village Green and see a group of Goblins running amok in the church. Go and help.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"east":"td_room 010", "north": "td_room 11"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"east":"to go to the elders house", "north": "to go to the church"},
               "vendor":[],
               "monster_list":[tutorial_goblin_rogue_001,tutorial_goblin_rogue_002],#Monster
               "enter_encounter_desc":"As you reach the pair locked in combat, you see the goblin thrust his hidden blade into an exposed part of the soldiers armour. He falls to the ground in pain and you realise that it is all up to you now. (Prepare for combat. In combat you will have four options. They will be displayed to you. Type the full name or the stated abbreviations to use them.)",
               "leave_encounter_desc":"The goblins lay dead at your feet.",            
               "go_to_stage":""
			}
			
	
			
td_room_01_010 = {
               "name":"Elders House", #
               "description":"You enter a small, humble home. The windows are smashed, the tables and chairs are over tunrned and there a clear sign of a struggle. A sturdy looking wooden box is on the floor, it has church key enscribed on it",
               "items":[TB_Church_key_001],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"td_room 09"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to go back to the village green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
			
td_room_01_011 = {
               "name":"Church Door", #
               "description":"Walking to the church you see the main door. It has sword slashes and claw marks all over it. Clearly some Goblins have tried to enter the church this way but failed. You notice an intricate lock just below the handle, if only you had a key to unlock it. You remember that the village elder keeps it safe. A fierce looking sword is on the floor. You think to yourself that this might make more sense to use for the battle that lays beyond these doors",
               "items":[],
               "item_auto_list":[TB_Tutorial_sword_001],
               "item_auto_take_list":[],
               "exits":{"unlock door":"td_room 12","south":"td_room 09"},
               "exit_req_inv":{"unlock door":["The Church Key"]},
               "exit_req_equ":{"unlock door":["Battered Sword"]},
               "exit_req_stat":{},
               "exit_action_desc":{"unlock door":"to unlock the door the church","south":"to go back to the village green"},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}

			
			
td_room_01_012 = {
               "name":"Church", #
               "description":"",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"explore":"td_room 13"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"explore":"to explore the church"},
               "vendor":[],
               "monster_list":[tutorial_goblin_fighters_001,tutorial_goblin_fighters_002],#Monster
               "enter_encounter_desc":"You enter the church and as the creaking door opens you hear the snarls of goblins growing louder as they rush toward you",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
			
td_room_01_013 = {
               "name":"Church Hall", #
               "description":"As you conclude there are no more goblins in the church you see a glowing orb of light emerging on the Village Green, like to one you remember reading about once. You remember that this is some type of magic and that creatures within the orb cannot be damaged by normal weapons. By some miracle there is a magic staff weapon right next to you. You take it, head into the glowing ball and hope for the best.",
               "items":[],
               "item_auto_list":[TB_Tutorial_Staff_001],
               "item_auto_take_list":[],
               "exits":{"south":"td_room 14"},
               "exit_req_inv":{},
               "exit_req_equ":{"south":["Old Staff"]},
               "exit_req_stat":{},
               "exit_action_desc":{"south":"go to the village green"},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
td_room_01_014 = {
               "name":"Village Green ", #3
               "description":"As the life fades away from the slain beasts the sphere of light fades away and you can see the last of the goblins being chased away by the mounted division of the town guard. The thought of your bed fills you mind and almost without thought you start walking home.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"south":"td_room 015"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"south":"to go home",},
               "vendor":[],
               "monster_list":[tutorial_goblin_mage_001,tutorial_orc_001 ],
               "enter_encounter_desc":"You walk into the village green and see an ominous sphere of glowing light",
               "leave_encounter_desc":"",            
               "go_to_stage":""
     		}

td_room_01_015 = {
               "name":"Home ", #2
               "description":"Your body aches and you stumble back into your home, which has luckily avoided any substancial damage. As you lumber toward your bed you realise that you still have three weapons on your person. As an attack like this may come again you decide it may be best to keep one. You think about which one you will keep",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"dagger":"td_room 017","sword":"td_room 016","staff":"td_room 018"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"dagger":"to become a rogue","sword":"to become a warrior","staff":"to become a mage"},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
			
td_room_01_016 = {
               "name":"Warrior Class", #
               "description":"You keep the Sword, hoping that trainng in one particular weapon and skill set will allow you to master it",
               "items":[],
               "item_auto_list":[Warrior_class],
               "item_auto_take_list":[],
               "exits":{"south":"td_room 19"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{""},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
			
td_room_01_017 = {
               "name":"Rogue Class", #
               "description":"You keep the Dagger, hoping that trainng in one particular weapon and skill set will allow you to master it",
               "items":[],
               "item_auto_list":[Rouge_class],
               "item_auto_take_list":[],
               "exits":{"south":"td_room 19"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{""},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}

	
td_room_01_018 = {
               "name":"Mage Class", #
               "description":"You keep the Staff, hoping that trainng in one particular weapon and skill set will allow you to master it",
               "items":[],
               "item_auto_list":[Mage_class],
               "item_auto_take_list":[],
               "exits":{"south":"td_room 19"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{""},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
		
td_room_01_019 = {
               "name":"Morning", #
               "description":"The morning sun peers through the window, you slowly awake and decide to go see in the light what the results of the carnage that last night brought",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"leave house":"td_room 20"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"leave house":"to go outside."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}

td_room_01_020 = {
               "name":"",
               "description":"",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{""},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{""},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":"stage2"
               }

#Stage2

rb_room_01_001 = {
               "name":"Village Green", #Link to Tutorial
               "description":"The Village Green looks completely different, the morning sun casts a harsh light on the black and grey ash. Villagers move around picking through the mess, salvaging what they can. You see a local militaman waving for your attention.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"talk":"rb_room 02", "east":"rb_room 32"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"talk":"to head over and talk to the Militiaman.", "east":"to go home."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}

rb_room_01_002 = {
               "name":"Militiaman",
               "description":"Good job last night! You managed to rout the stragglers who got passed us. Please follow me to the Barracks, we've pulled a few things together to offer as thanks.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"follow":"rb_room 03", "return":"first room"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"return":"to return to the Village Green.", "follow":"to follow the Militiaman to the Barracks."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}

rb_room_01_003 = {
               "name":"Barracks",
               "description":"The Barracks are a mess, injured lie in beds and broken weapons lie scattered on the floor. The Quatermaster spots your entrance and hands you a hefty pack. Without a word, he return to attending his men.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"open":"rb_room 06", "pack":"rb_room 07", "reward":"rb_room 08", "east":"rb_room 05"},
               "exit_req_inv":{"open":["mage path"], "pack":["fighter path"], "reward":["rogue path"]},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"open":"to open the pack.", "pack":"to open the pack.", "reward":"to open the pack.", "east":"to return to Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
			   
			   
rb_room_01_004 = {
               "name":"Village Green",
               "description":"The Village Green looks completely different, the morning sun casts a harsh light on the black and grey ash. The Villagers are taking a break, it's hard work.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 12", "east":"rb_room 33"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to go to the Barracks.", "east":"to go home."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}	
				
rb_room_01_005 = {
               "name":"Village Green",
               "description":"The Village Green looks completely different, the morning sun casts a harsh light on the black and grey ash. The Villagers are taking a break, it's hard work. Remember to open your reward.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"open":"rb_room 09", "sack":"rb_room 10", "reward":"rb_room 11", "west":"rb_room 15", "east":"rb_room 34"},
               "exit_req_inv":{"open":["mage path"], "sack":["fighter path"], "reward":["rogue path"]},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"open":"to open the pack.", "pack":"to open the pack.", "reward":"to open the pack.", "west":"to go to the Barracks.", "east":"to go home."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}	
				
rb_room_01_006 = {
               "name":"Sack",
               "description":"You open the sack. Inside you find a gnarled Wizard Staff, faded Apprentice Robes and a note. The note ask that you go see the Milita Captain in his office.",
               "items":[],
               "item_auto_list":[TB_wooden_staff_001, TB_novice_robes_001], #Staff, Robes.
               "item_auto_take_list":[],
               "exits":{"office":"rb_room 13", "east":"rb_room 04"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"office":"to see the Militia Captain in his office.", "east": "to return to Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}
				
rb_room_01_007 = {
               "name":"Sack",
               "description":"You open the sack. Inside you find a pitted Longsword, dusty Fighting Leathers and a note. The note ask that you go see the Milita Captain in his office.",
               "items":[],
               "item_auto_list":[TB_steel_sword_001, TB_old_Armour_001], #Sword, Leather.
               "item_auto_take_list":[],
               "exits":{"office":"rb_room 13", "east":"rb_room 04"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"office":"to see the Militia Captain in his office.", "east":"to return to Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}
				
rb_room_01_008 = {
               "name":"Sack",
               "description":"You open the sack. Inside you find a rusted dagger, worn Light Armour and a note. The note ask that you go see the Milita Captain in his office.",
               "items":[],
               "item_auto_list":[TB_steel_dagger_001, TB_Leather_Armour_001],#Dagger, Armour.
               "item_auto_take_list":[],
               "exits":{"office":"rb_room 13", "east":"rb_room 04"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"office":"to see the Militia Captain in his office.", "east":"to return to Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}	
				
rb_room_01_009 = {
               "name":"Sack",
               "description":"You open the sack. Inside you find a gnarled Wizard Staff, faded Apprentice Robes and a note. The note ask that you go see the Milita Captain in his office.",
               "items":[],
               "item_auto_list":[TB_wooden_staff_001, TB_novice_robes_001], #Staff, Robes.
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 12", "east":"rb_room 33"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to go to the Barracks.", "east":"to go home."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}
				
rb_room_01_010 = {
               "name":"Sack",
               "description":"You open the sack. Inside you find a pitted Longsword, dusty Fighting Leathers and a note. The note ask that you go see the Milita Captain in his office.",
               "items":[],
               "item_auto_list":[TB_steel_sword_001, TB_old_Armour_001], #Sword, Leather.
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 12", "east":"rb_room 33"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to go to the Barracks.", "east":"to go home."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}
				
rb_room_01_011 = {
               "name":"Sack",
               "description":"You open the sack. Inside you find a rusted dagger, worn Light Armour and a note. The note ask that you go see the Milita Captain in his office.",
               "items":[],
               "item_auto_list":[TB_steel_dagger_001, TB_Leather_Armour_001], #Dagger, Armour.
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 12", "east":"rb_room 33"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to go to the Barracks.", "east":"to go home."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}
				
rb_room_01_012 = {
               "name":"Barracks",
               "description":"The Barracks are a mess, injured lie in beds and broken weapons lie scattered on the floor. The Militia Captain is expecting you in his Office.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"office":"rb_room 13", "east":"rb_room 04"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"office":"to see the Militia Captain in his office.", "east":"to return to Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}
				
rb_room_01_013 = {
               "name":"Militia Captain",
               "description":"Jolly good showing last night Chap! You gave 'em what for and all. Think you can rustle 'em up a bit more for us? We would, but my men have been roughed up a tad too much. Head over to the cave north o' here, that's where the Orc Chief is lurking. Kill him for me, I'll make sure to make it worth your time.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"east":"rb_room 16", "barracks":"rb_room 14"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"east":"to head to the Village Green.", "barracks":"to return to the Barracks."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}
			
rb_room_01_014 = {
               "name":"Barracks",
               "description":"The Barracks are improving. Men are patched up and the weapons have been stowed away.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"office":"rb_room 13", "east":"rb_room 16"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"office":"to see the Militia Captain in his office.", "east":"to return to Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""	
			}
	
rb_room_01_015 = {
               "name":"Barracks",
               "description":"The Barracks are a mess, injured lie in beds and broken weapons lie scattered on the floor. Remember to open your reward.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"open":"rb_room 06", "pack":"rb_room 07", "reward":"rb_room 08","east":"rb_room 05"},
               "exit_req_inv":{"open":["mage path"], "pack":["fighter path"], "reward":["rogue path"]},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"open":"to open the pack.", "pack":"to open the pack.", "reward":"to open the pack.", "east": "to return to Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
				
rb_room_01_016 = {
               "name":"Village Green",
               "description":"It's Midday and the Villagers seem to have collected themselves. You can see the vendor from the night before and the Elder's door is open.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"east":"rb_room 35", "vendor":"rb_room 17", "south":"rb_room 18", "north":"rb_room 20", "west":"rb_room 14"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"east":"to go home.", "vendor":"to talk to the vendor.", "south":"to go to the Elder's house.", "west":"to go to the Barracks."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
				
rb_room_01_017 = {
               "name":"Vendor",
               "description":"Thank you for saving me last night! Here take this Health Potion, maybe it can save you one day. Would you like to see my wares?",
               "items":[],
               "item_auto_list":[TB_pot_002], #Health Potion.
               "item_auto_take_list":[],
               "exits":{"return":"rb_room 16"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"return":"to return to the Village Green."},
               "vendor":[TB_village_merchant_001], #Vendor
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
				
rb_room_01_018 = {
               "name":"Elder's House",
               "description":"The place looks much better than last night. The Elder is pottering around the house, muttering something about missing keys.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"return":"rb_room 16", "talk":"rb_room 19"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"return":"to return to the Village Green.", "talk":"to talk to the Village Elder."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
rb_room_01_019 = {
               "name":"Elder",
               "description":"You're going to go clear out the monsters, eh? On your way through the forest look out for my hidden cache. I put some useful stuff in there in my youth. Here, this map will show you the way.",
               "items":[],
               "item_auto_list":[TB_elder_map_001], #map
               "item_auto_take_list":[],
               "exits":{"return":"rb_room 18"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"return":"to return to the Elder's House."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
			}
				
rb_room_01_020 = {
               "name":"Forest", #Link to Dungeon
               "description":"Destruction lies everywhere. Proof of the nearby monsters.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 21", "east":"pc_room 01"},
               "exit_req_inv":{"west":["map"]},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to find the hidden cache.", "east":"to the cave entrance."},
               "vendor":[],
               "monster_list":[wolf_001, wolf_002], #Wolf
               "enter_encounter_desc":"A Mangy Wolf pounces at you!",
               "leave_encounter_desc":"The Wolf was mad, it had to be put down.",            
               "go_to_stage":""
			}
				
rb_room_01_021 = {
                "name":"Hidden Cache",
               "description":"You find a small chest hidden in the bole of a tree.",
               "items":["GOLD x 25", TB_pot_005], #GOLD, Health Potion.
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"east":"rb_room 20"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"east":"to retrun to the Forest."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_022 = {
                "name":"Village Green", #Link to Dungeon
               "description":"The Villagers have been hard at work. The Village looks spotless.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"vendor":"rb_room 23", "south":"rb_room 24", "west":"rb_room 36", "west":"rb_room 25"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"vendor":"to talk to the vendor.", "south":"to the Elder's House.", "east":"to head home.", "west":"to go to the Barracks"},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_023 = {
                "name":"Vendor",
               "description":"Any luck clearing out the monsters? I managed to get my stock all together, wanna see?",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"return":"rb_room 22"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"return":"to retrun to the Village Green."},
               "vendor":[TB_village_merchant_002], #vendor
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_024 = {
                "name":"Elder House",
               "description":"The door is locked, you can hear thunderous snoring from beyond. The Elder must be asleep.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"north":"rb_room 22"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"north":"to retrun to the Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_025 = {
                "name":"Barracks",
               "description":"The militamen see your return and raise a big cheer. The Captain is waiting for you in his office.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"office":"rb_room 26"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"office":"to enter the office."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_026 = {
                "name":"Militia Captain",
               "description":"Spiffing job out there m'boy! They didn't stand a chance! The Village is in your debt. Take this, a token of our thanks.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"accept":"rb_room 27", "reward":"rb_room 28", "thanks":"rb_room 29"},
               "exit_req_inv":{"accept":["mage path"], "reward":["fighter path"], "thanks":["rogue path"]},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"accept":"to accept the reward.", "reward":"to accept the reward.", "thanks":"to accept the reward."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_027 = {
                "name":"Reward",
               "description":"The Militia Captain hands you a sleek new staff, you can feel it thrumming with power.",
               "items":[], #Robes
               "item_auto_list":[TB_fine_Staff_001],
               "item_auto_take_list":[],
               "exits":{"continue":"rb_room 30"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"continue":"to continue talking to the Captain."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_028 = {
                "name":"Reward",
               "description":"The Militia Captain hands you a sharp new sword, it has your initials on the hilt.",
               "items":[], #Armour
               "item_auto_list":[TB_fine_sword_001],
               "item_auto_take_list":[],
               "exits":{"continue":"rb_room 30"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"continue":"to continue talking to the Captain."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_029 = {
                "name":"Reward",
               "description":"The Militia Captain hands you a well-balanced dagger, the edge is razor sharp.",
               "items":[], #Dagger
               "item_auto_list":[TB_fine_dagger_001],
               "item_auto_take_list":[],
               "exits":{"continue":"rb_room 30"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"continue":"to continue talking to the Captain."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_030 = {
                "name":"Militia Captain",
               "description":"Now head on home, m'boy. You deserve a long rest. I'll be in touch if we need you.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"home":"rb_room 31"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"home":"to head home."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_031 = {
                "name":"The End",
               "description":"Well Done, You've Completed the Game!",
               "items":[],
               "item_auto_list":[TB_victory_001],
               "item_auto_take_list":[],
               "exits":{""},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{""},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""#stage complete
               }
				
rb_room_01_032 = {
                "name":"Home",
               "description":"You're house is a mess. What kind of hero has a messy bedroom?!",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"weast":"rb_room 01"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to head to the Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_033 = {
                "name":"Home",
               "description":"Did you leave cheese out?! Oh no, that's just your laundry...",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 04"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to head to the Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_034 = {
                "name":"Home",
               "description":"Did you leave cheese out?! Oh no, that's just your laundry...",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 05"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to head to the Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_035 = {
                "name":"Home",
               "description":"You have pets? Oops, sorry. It's just a rat.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 16"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to head to the Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }
               
rb_room_01_036 = {
                "name":"Home",
               "description":"Seriously, it would take a heroic feat just to live here.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 22"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to head to the Village Green."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

pc_room_01_001 = {"name":"Cave Mouth",
               "description":"A small crack in the side of a cliff, leading into a cave.",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 20","enter":"pc_room 02"},
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":{"west":"to the forest.","enter":"into the cave."},                            
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",
               "go_to_stage":""
               }

pc_room_01_002 = {"name":"Cavern",
               "description":"You find yourself in a large cavern with three dark passages leading deeper into the cave. One to your left, one on your right and one in the middle.",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"leave":"pc_room 01","left":"pc_room 03","forward":"pc_room 08","right":"pc_room 04","den":"pc_room 07"},
               "exit_req_inv":{"right":["Has not entered Den"],"den":["Has entered Den"]},
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":{"leave":"to go back to the cave mouth.","left":"to the golbins stash.","right":"to go to the den.","den":"to go to the den.","middle":"to a tight cave bottleneck."},
               "vendor":{},
               "monster_list":[goblin_warrior_001,goblin_warrior_002,orc_001],
               "enter_encounter_desc":"You are spotted by the guards, they charge at you!",
               "leave_encounter_desc":"You manage to defeat the guards without alerting the rest of the cave!",            
               "go_to_stage":""
               }

pc_room_01_003 = {"name":"Stash",
               "description":"A small room filled with rusty weapons and dynamite.",
               "item_list":[Dynamite],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"leave":"pc_room 02"},
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":{"leave":"to go back to the cavern."},
               "vendor":{},
               "monster_list":[giant_rat_001,goblin_thief_001],
               "enter_encounter_desc":"You are jumped by a goblin thief and his guard rat!",
               "leave_encounter_desc":"You kill the stash guards!",            
               "go_to_stage":""
               }

pc_room_01_004 = {"name":"Den",				# Uncleared, two options to go to
               "description":"The living area for the goblins, as you walk to the middle of the room you notice a goblin turn in his bed.",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"steal":"pc_room 05","leave":"pc_room 06"},
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":{"steal":"DEX,7"},
               "exit_action_desc":{"steal":"the gold from the sleeping goblins","leave":"to the cavern."},
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"You are jumped by a goblin thief and his guard rat!",
               "leave_encounter_desc":"You kill the stash guards",            
               "go_to_stage":""
               }

pc_room_01_005 = {"name":"Den",				# Managed to sneak out
               "description":"You manage to sneak around and steal the gold from the sleeping goblins.",
               "item_list":["GOLD x 20"],
               "item_auto_list":[TB_Den_key_002],
               "item_auto_take_list":["Has entered Den"],
               "exits":{"leave":"pc_room 02"},
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":{"leave":"to the cavern."},
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

pc_room_01_006 = {"name":"Den",				# Woke up golbins
               "description":"The living area for the goblins, every goblin here is dead, you see nothing else of value here.",
               "item_list":[],
               "item_auto_list":[TB_Den_key_002],
               "item_auto_take_list":["Has entered Den"],
               "exits":{"leave":"pc_room 02"},
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":{"leave":"to the cavern"},
               "vendor":{},
               "monster_list":[goblin_thief_002,goblin_warrior_003],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

pc_room_01_007 = {"name":"Den",				# Cleared den
               "description":"The living area for the goblins, you see nothing else of value here.",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"leave":"pc_room 02"},
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":{"leave":"to the cavern"},
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

pc_room_01_008 = {"name":"Bottle Neck",
               "description":"A very small passage, recently blocked by bolders.",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"back":"pc_room 02","explode":"pc_room 09","push":"pc_room 09"},
               "exit_req_inv":{"explode":["Dynamite"]},
               "exit_req_equ":[],
               "exit_req_stat":{"push":["str,7"]},
               "exit_action_desc":{"back":"to the cavern.","explode":"the bolders, to free the passage.","push":"the rocks out the way."},
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

pc_room_01_009 = {"name":"Chamber",
               "description":"A large cave, the orcs lay dead around you.",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"leave":"pc_room 10"},
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":{"leave":"the cave."},
               "vendor":{},
               "monster_list":[orc_002,orc_chief_001],
               "enter_encounter_desc":"As you walk in, the orc chief spots you and roar",
               "leave_encounter_desc":"You slay the orc chief",            
               "go_to_stage":""
               }

pc_room_01_010 = {"name":"Cave Mouth",
               "description":"A small crack in the side of a cliff, leading into a cave.",
               "item_list":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"west":"rb_room 22"},
               "exit_req_inv":[],
               "exit_req_equ":[],
               "exit_req_stat":[],
               "exit_action_desc":{"west":"to the village green"},
               "vendor":{},
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }