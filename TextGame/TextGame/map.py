from items import *
from monsters import *
from vendors import *
#hoping that this forces an update
#Stage 1 rooms
dh_room_01_001 = {
               "name":"Your House",
               "description":"Waking in your room, you wipe the sleep from your eyes and can hear a commotion from outside. Screams, snarls and crashes. Perhaps someone needs a snickers?",
               "items":[dh_sword_001,dh_leather_armour_001],
               "item_auto_list":[class_fighter],
               "item_auto_take_list":[],
               "exits":{"head outside":"Room 2"},
               "exit_req_inv":{},
               "exit_req_equ":{"head outside":["Demo Sword","Leather Armour"]},
               "exit_req_stat":{},
               "exit_action_desc":{"head outside":"to investgate the noise."},
               "vendor":[],
               "monster_list":[],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

dh_room_01_002 = {
               "name":"The village square",
               "description":"Your house leads on to the village square. What usually is a prety and peaceful green area has been stained red with the blood of many of the people you've grown up with. \n The goblins must be coming in from the village gate.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"defend":"Room 3"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"defend":"to head to the village gate and stop the pillaging"},
               "vendor":[dh_vendor_001],
               "monster_list":[dh_goblin_001,dh_goblin_002],
               "enter_encounter_desc":"Two goblins stand over your neighbour , their mouths dripping with blood. They scramble towards you.",
               "leave_encounter_desc":"The goblins ley moitionless on the ground, much like the body they feasted on moments before they attacked",            
               "go_to_stage":""
               }
dh_room_01_003 = {
               "name":"The Village Gate",
               "description":"The goblins have routed and you have fended off the attack. Many have died but many survied! This is true on both sides of the battle however and it clears there is likely to be more attacks like this to come. \n The village leader approaches you and thanks you.",
               "items":[],
               "item_auto_list":[],
               "item_auto_take_list":[],
               "exits":{"into the woods":"Room 4"},
               "exit_req_inv":{},
               "exit_req_equ":{},
               "exit_req_stat":{},
               "exit_action_desc":{"into the woods":"to go forth and look for where the orcs may have come from."},
               "vendor":[],
               "monster_list":[dh_orc_001],
               "enter_encounter_desc":"",
               "leave_encounter_desc":"",            
               "go_to_stage":""
               }

dh_room_01_004 = {
               "name":"To Stage 2",
               "description":"This should not be shown",
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
               "go_to_stage":"Stage 2"
               }

dh_room_02_001 = {
               "name":"Woods Entrance",
               "description":"This should not be shown",
               "items":[],
               "item_auto_list":[victory_token],
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