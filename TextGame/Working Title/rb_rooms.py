rb_room_01_001 = {
               "name":"Village Green", #Link to Tutorial
               "description":"The Village Green looks completely different, the morning sun casts a harsh light on the black and grey ash. Villagers move around picking through the mess, salvaging what they can. You see a local militaman waving for your attention.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"talk":"rb_Room 02", "east":"rb_Room 32"},
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
               "exits":{"follow":"rb_Room 03", "return":"first room"},
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
               "exits":{"open":"rb_Room 06", "pack":"rb_Room 07", "reward":"rb_Room 08", "east":"rb_Room 05"},
               "exit_req_inv":{"open":"mage path", "pack":"fighter path", "reward":"rogue path"},
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
               "exits":{"west":"rb_Room 12", "east":"rb_Room 33"},
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
               "exits":{"open":"rb_Room 09", "sack":"rb_Room 10", "reward":"rb_Room 11", "west":"rb_Room 15", "east":"rb_Room 34"},
               "exit_req_inv":{"open":"mage path", "sack":"fighter path", "reward":"rogue path"},
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
               "item_auto_list":[], #Staff, Robes.
               "item_auto_take_list":[],
               "exits":{"office":"rb_Room 13", "east":"rb_Room 04"},
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
               "item_auto_list":[], #Sword, Leather.
               "item_auto_take_list":[],
               "exits":{"office":"rb_Room 13", "east":"rb_Room 04"},
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
               "item_auto_list":[],#Dagger, Armour.
               "item_auto_take_list":[],
               "exits":{"office":"rb_Room 13", "east":"rb_Room 04"},
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
               "item_auto_list":[], #Staff, Robes.
               "item_auto_take_list":[],
               "exits":{"west":"rb_Room 12", "east":"rb_Room 33"},
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
               "item_auto_list":[], #Sword, Leather.
               "item_auto_take_list":[],
               "exits":{"west":"rb_Room 12", "east":"rb_Room 33"},
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
               "item_auto_list":[], #Dagger, Armour.
               "item_auto_take_list":[],
               "exits":{"west":"rb_Room 12", "east":"rb_Room 33"},
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
               "exits":{"office":"rb_Room 13", "east":"rb_Room 04"},
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
               "exits":{"east":"rb_Room 16", "barracks":"rb_Room 14"},
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
               "exits":{"office":"rb_Room 13", "east":"rb_Room 16"},
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
               "exits":{"open":"rb_Room 06", "pack":"rb_Room 07", "reward":"rb_Room 08" "east":"rb_Room 05"},
               "exit_req_inv":{"open":"mage path", "pack":"fighter path", "reward":"rogue path"},
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
               "exits":{"east":"rb_Room 35", "vendor":"rb_Room 17", "south":"rb_Room 18", "north":"rb_Room 20", "west":"rb_Room 14"},
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
               "item_auto_list":[], #Health Potion.
               "item_auto_take_list":[],
               "exits":{"return":"rb_Room 16"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"return":"to return to the Village Green."},
               "vendor":[], #Vendor
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
               "exits":{"return":"rb_Room 16", "talk":"rb_Room 19"},
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
               "item_auto_list":[], #map
               "item_auto_take_list":[],
               "exits":{"return":"rb_Room 18"},
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
               "exits":{"west":"rb_Room 21", "east":"pc_Room 01"},
               "exit_req_inv":{"west":"hidden_map"},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"west":"to find the hidden cache.", "east":"to the cave entrance."},
               "vendor":[],
               "monster_list":[], #Wolf
               "enter_encounter_desc":"A Mangy Wolf pounces at you!",
               "leave_encounter_desc":"The Wolf was mad, it had to be put down.",            
               "go_to_stage":""
			}
				
rb_room_01_021 = {
                "name":"Hidden Cache",
               "description":"You find a small chest hidden in the bole of a tree.",
               "items":[], #GOLD, Health Potion.
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"east":"rb_Room 20"},
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
               "exits":{"vendor":"rb_Room 23", "south":"rb_Room 24", "west":"rb_Room 36", "west":"rb_Room 25"},
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
               "exits":{"return":"rb_Room 22"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"return":"to retrun to the Village Green."},
               "vendor":[], #vendor
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
               "exits":{"north":"rb_Room 22"},
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
               "exits":{"office":"rb_Room 26"},
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
               "exits":{"accept":"rb_Room 27", "reward":"rb_Room 28", "thanks":"rb_Room 29"},
               "exit_req_inv":{"accept":"mage path", "reward":"fighter path", "thanks":"rogue path"},
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
               "items":[], #Staff
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"continue":"rb_Room 30"},
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
               "items":[], #Sword
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"continue":"rb_Room 30"},
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
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"continue":"rb_Room 30"},
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
               "exits":{"home":"rb_Room 31"},
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
               "go_to_stage":""#stage complete
               }
				
rb_room_01_032 = {
                "name":"Home",
               "description":"You're house is a mess. What kind of hero has a messy bedroom?!",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"weast":"first room"},
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
               "exits":{"west":"rb_Room 04"},
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
               "exits":{"west":"rb_Room 05"},
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
               "exits":{"west":"rb_Room 16"},
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
               "exits":{"west":"rb_Room 22"},
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

        
stage1 = {"first room":rb_room_01_001,#Link to Tutorial
          "rb_Room 02":rb_room_01_002,
          "rb_Room 03":rb_room_01_003,
		"rb_Room 04":rb_room_01_004,
		"rb_Room 05":rb_room_01_005,
		"rb_Room 06":rb_room_01_006,#Items
		"rb_Room 07":rb_room_01_007,#Items
		"rb_Room 08":rb_room_01_008,#Items
		"rb_Room 09":rb_room_01_009,#Items
		"rb_Room 10":rb_room_01_010,#Items
		"rb_Room 11":rb_room_01_011,#Items
		"rb_Room 12":rb_room_01_012,
		"rb_Room 13":rb_room_01_013,
		"rb_Room 14":rb_room_01_014,
		"rb_Room 15":rb_room_01_015,
          "rb_Room 16":rb_room_01_016,
          "rb_Room 17":rb_room_01_017,#Health Potion, Vendor
          "rb_Room 18":rb_room_01_018,
          "rb_Room 19":rb_room_01_019,#Map
          "rb_Room 20":rb_room_01_020,#Link to Dungeon, Wolf
          "rb_Room 21":rb_room_01_021,#Items
          "rb_Room 22":rb_room_01_022,#Link to Dungeon
          "rb_Room 23":rb_room_01_023,#Vendor
          "rb_Room 24":rb_room_01_024,
          "rb_Room 25":rb_room_01_025,
          "rb_Room 26":rb_room_01_026,
          "rb_Room 27":rb_room_01_027,#Items
          "rb_Room 28":rb_room_01_028,#Items
          "rb_Room 29":rb_room_01_029,#Items
          "rb_Room 30":rb_room_01_030,
          "rb_Room 31":rb_room_01_031,#Stage Complete
          "rb_Room 32":rb_room_01_032,
          "rb_Room 33":rb_room_01_033,
          "rb_Room 34":rb_room_01_034,
          "rb_Room 35":rb_room_01_035,
          "rb_Room 36":rb_room_01_036
          }