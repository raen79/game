#forcechange
#!/usr/bin/python3
from random import randint
from getpass import getpass

from player import *
from command_parser import *
from os import getcwd
from os import chdir
from os import listdir
from os import path
from importlib import import_module

game = {}
#Main Menu Functions________

def main_menu(in_progress = False):
    print("""    ___                                                                   _ 
   /   \ _   _  _ __    __ _   ___   ___   _ __   ___    __ _  _ __    __| |
  / /\ /| | | || '_ \  / _` | / _ \ / _ \ | '_ \ / __|  / _` || '_ \  / _` |
 / /_// | |_| || | | || (_| ||  __/| (_) || | | |\__ \ | (_| || | | || (_| |
/___,'   \__,_||_| |_| \__, | \___| \___/ |_| |_||___/  \__,_||_| |_| \__,_|
                       |___/                                                
        ___  _        _    _                             _                  
       /   \(_)  ___ | |_ (_)  ___   _ __    __ _  _ __ (_)  ___  ___       
      / /\ /| | / __|| __|| | / _ \ | '_ \  / _` || '__|| | / _ \/ __|      
     / /_// | || (__ | |_ | || (_) || | | || (_| || |   | ||  __/\__ \      
    /___,'  |_| \___| \__||_| \___/ |_| |_| \__,_||_|   |_| \___||___/      
                                                                      
    ________________________________________________________________________
    
    A Text Based RPG Sandbox - 'The sword of Azeroth' and other stories""")


    print("")
    if len(game)>0:
        print("Current Game:" + game["name"])
        print("")
        print("About this game:")
        print("")
        print(game["description"])
        

    else:
        print("Current Game: -- none loaded -- ")
        print("")
        print("About this game:")
        print("")
        print("")

    print("Choose an option:")
    
    options_list = []

    if len(game)>0:
        if in_progress:
            options_list.append("Resume Game")
            options_list.append("Restart Game")
        else:
            options_list.append("Play Game")
    options_list.append("Load Game")
    options_list.append("About")
    options_list.append("Exit")

    menu_item_count = 1

    for item in options_list:
        print(str(menu_item_count) + " - " + item)
        menu_item_count +=1

    print("")

    need_input = True

    while need_input:
        menu_input = input(">")
        try:
            input_int = int(menu_input)
            menu_input = options_list[input_int -1]
        except:
            pass

        menu_command = menu_input.split(" ")[0].lower()
        if menu_command == "resume":
            need_input = False
            return menu_resume()
        elif menu_command == "restart":
            need_input = False
            return menu_restart()
        elif menu_command == "play":
            need_input = False
            return menu_play()
        elif menu_command == "load":
            need_input = False
            return menu_load()
        elif menu_command == "about":
            need_input = False
            return menu_about()
        elif menu_command == "exit":
            need_input = False
            return menu_exit()
            
        else:
            print("")
            print("Input not recognised")
        

def menu_resume():
    return "game"


def menu_restart():
    clear_game_data()
    gamedir = "Dungeons_and_Dictionaries"
    import_game_data(gamedir)

def menu_play():
    return "game"

 
def menu_load():
    clear_game_data()
    #gamedir = "Dungeons_and_Dictionaries"
    gamedir = get_game_dir()
    import_game_data(gamedir)

def get_game_dir():
    need_input = True

    

    while need_input:
        print("_________________________")
        print("")
        game_list = print_games()
        print("")
        print("Enter the number of the game you would like to load")
        menu_input = input(">")
        try:
            input_int = int(menu_input)
            
            if len(game_list) >= input_int:
                return game_list[input_int -1]
            else:
                print("")
                print("Not a valid game number")
        except:
            print("")
            print("Not a valid game number")

def print_games():
   current_dir = getcwd()
   import_dir = current_dir + "\\Games"
  
   game_dirs =[]
   for filename in listdir(import_dir):
       if path.isdir(import_dir +"\\"+filename) and filename != "__pycache__":
           game_dirs.append(filename)
  
   print("")
   print("Available Games:")
   print("")
   game_count = 1
   for filename in game_dirs:
        print(str(game_count) +" - " + filename)
        game_count +=1
   
   return game_dirs
   
            

 
def menu_about():
    print("________________________")
    print("")
    print("ABOUT")
    print("")
    print("Dungeons and Dictionaries content system developed by:")
    print('Tim Bird')
    print('Rhys BeckettMobile')
    print('Ajay Boby')
    print('Pete Clark')
    print('Thomas Darwin')
    print('Daniel Harborne')
    print('Eran Peer')
    print("")
    print("Hit enter to return to menu")
    input("")

def menu_exit():
    print("")
    print("Thanks for playing!")
    return "exit"


def import_game_data(folder_name):
   current_dir = getcwd()
   import_dir = current_dir + "\\Games\\" + folder_name
   chdir(import_dir)
   #for filename in listdir(getcwd()):
   #    print(filename)
   #input("")


   #test =import_module("game")

   #test = __import__('game',globals(),locals())
   test = __import__('Games.Dungeons_and_Dictionaries.game',globals(),locals())
   test = test.__dict__[folder_name].__dict__["game"]

   for k in dir(test):
       globals()[k] = test.__dict__[k]

   chdir(current_dir)

def import_local_game():
   test = __import__('game',globals(),locals())

   for k in dir(test):
       globals()[k] = test.__dict__[k]


def clear_game_data():
    dict_list = []
    #other_list = []

    dict_ignore_list=["__builtins__"]

    for item in globals():
       #print(item + " " + str(type(globals()[item])))
       if type(globals()[item]) is dict:
           if not(str(item) in dict_ignore_list):
                dict_list.append(str(item))
                
    #   else:
    #       if not(callable(globals()[item])):
    #        other_list.append(str(item))


    #print("_____")
    #print("Dictionaries:")
    #dict_list.sort()
    for item in dict_list:
        #print(item)
        del globals()[item]
    
    #print("_____")
    #print("Other:")
    #other_list.sort()
    #for item in other_list:
    #  print(item)




#General Game Functions______

god_mode = False



def move_stage_check():
    global current_room
    global current_stage
    if len(current_room["go_to_stage"]) > 0:
        current_stage = game["stages"][current_room["go_to_stage"]]
        current_room = current_stage["first room"]

def player_death():
    global current_room
    global previous_room
    global player
    print("you have died!!")
    current_room = previous_room

    player["current_health"] = player["max_health"]
    
def check_for_victory():

    return check_player_has_item(player,"end game token")
        
def initialise_game():
    global current_stage
    global current_room   
    global previous_room
    
    current_stage = game["stages"][game["start_stage"]]
    current_room = current_stage[game["start_room"]]
    calculate_working_stats(player)
    player["current_health"] = player["max_health"]

def enter_room_check():
    
    move_stage_check()
    
    if len(current_room["monster_list"]) > 0:
        encounter_loop()
    
    
    room_auto_give(current_room)    

    room_auto_take(current_room)

    #enter room loop
    pass

def room_auto_take(room):
    global player

    
    for room_item in room["item_auto_take_list"]:
        #check if each inventory item has the same name as the auto remove item. if it does remove it.
        for inv_item in player["inventory"]:
            if inv_item["name"] == room_item["name"]:
                player["inventory"].remove(inv_item)

    #check if the equipped items have the same name as the auto remove item. if either do remove it.
        if len(player["weapon"]) >0:
            if player["weapon"]["name"] == room_item["name"]:
                player["weapon"] = {}

        if len(player["armour"]) >0:
            if player["armour"]["name"] == room_item["name"]:
                player["armour"] = {}

def room_auto_give(room):
    global player


    for room_item in room["item_auto_list"]:
        #if an item matching the room auto item is not found in the player's inventory , equipped weapon or armour then give the player the item.
        if not(room_item in player["inventory"]) and player["armour"] != room_item and player["weapon"] != room_item:
            player["inventory"].append(room_item)

def calculate_monster_combat_mod(monster):
    combat_stat = 0
    weapon_value = 0

    combat_stat_key = monster["combat_stat"]
    if combat_stat_key != "STR" and combat_stat_key != "DEX" and combat_stat_key != "INT":
        combat_stat_key = "STR"

    base_value = monster["stat_dict"][combat_stat_key]

    equiped_weapon = monster["weapon"]
    if len(equiped_weapon) > 0:
        weapon_value = equiped_weapon["stat_dict"][combat_stat_key]

    combat_stat = base_value + weapon_value
    return combat_stat

#Combat Functions____________

#end combat functions___
def calculate_encounter_exp(defeated_monsters):

        total_exp_gain = 0
        for monster in defeated_monsters:
            total_exp_gain += calculate_exp_gain(player,monster["level"])
        print("You gained "+ str(total_exp_gain) +" exp from the encounter!")
        player_gain_exp(player,total_exp_gain)

def generate_loot(defeated_monsters):
    global current_room
    global player
    loot_items = []
    for monster in defeated_monsters:
        for loot_table in monster["loot"]:
            loot = random_loot(loot_table)
            if type(loot) is int:
                player["gold"] += loot
            elif type(loot) is str:
                pass
            else:    
                loot_items.append(loot)

    #currently loot is dropped on the floor 
    return loot_items

def random_loot(loot_table):
    loot_int = randint(0,99)

    for k,v in sorted(loot_table.items()):
        if loot_int <= k:
            if type(v) is str:
                try:
                    gold = int(v.replace("GOLD x ",""))
                    return gold
                except:
                    return int(0)
            else:
                return v

    return ""

#main combat functions____
def print_combat_summary(monster_list,defeated_monsters,current_monster):
    
    global player
    
    print("_______________")
    print("")
    print("Your Health: "+str(player["current_health"]))
    print("")

    print("Monster Group:")

    first_monster = True
    for monster in monster_list:
        monster["current_combat_mod"] = calculate_monster_combat_mod(monster)
        if first_monster:
            print("  "+monster["name"] +" - hp:"+str(monster["current_health"])+" <- currently fighting")
            first_monster = False
        else:
            print("  "+monster["name"] +" - hp:"+str(monster["current_health"]))
    print("Defeated Monsters:")
    print("")

    for monster in defeated_monsters:
        print("  "+monster["name"])
    
    print("")
    print("current foe:")
    print(current_monster["name"])
    print(current_monster["description"])
    print("")
    print("_______________")

def get_player_action():
    need_input = True

    while need_input:
        print("Make your move: (light attack[la], heavy attack[ha], parry[p], dodge[d])")
        user_action = str(input(">"))
        
        if user_action.lower() == "light attack" or user_action.lower() == "la":
            return "light attack"
        elif user_action.lower() == "heavy attack" or user_action.lower() == "ha":
            return "heavy attack"
        elif user_action.lower() == "parry" or user_action.lower() == "p":
            return "parry"
        elif user_action.lower() == "dodge" or user_action.lower() == "d":
            return "dodge"
        else:
            print("that is not a valid action")
            print("")

def get_monster_action(monster,skip):
    
    action = ""

    need_action = True
    while need_action:
        action_int = randint(0,99)
        for k,v in sorted(monster["combat_dict"].items()):
            if action_int <= k:
                action = v
                break
            else:
                action = "inaction"
        if skip !="player":
            need_action = False
        else:
            if action != "dodge" and action != "parry":
                need_action = False 

    
    return action

def player_attack_monster(atk_type,monster):
    global player
    weapon_damage = 0
    
    if len(player["weapon"]) > 0:
        weapon_damage = randint(player["weapon"]["min_dmg"],player["weapon"]["max_dmg"]) 

    damage = player["current_combat_mod"] + weapon_damage

    if atk_type == "heavy":
        damage *= 2

    if len(monster["armour"]) > 0:
        damage -= monster["armour"]["armour value"]

    monster["current_health"] -= damage

    print("You hit your foe for " +str(damage)+" damage!")
    
def monster_attack_player(atk_type,monster):
    global player
    weapon_damage = 0
    
    if len(monster["weapon"]) > 0:
        weapon_damage = randint(monster["weapon"]["min_dmg"],monster["weapon"]["max_dmg"]) 

    damage = monster["current_combat_mod"] + weapon_damage


    if atk_type == "heavy":
        damage *= 2

    if len(player["armour"]) > 0:
        damage -= player["armour"]["armour value"]
    
    damage_player(player,damage)

    print("Your foe hits you for " +str(damage)+" damage!")

def player_parry_monster(monster):
    global player

    damage = player["stat_dict"]["DEX"]

    monster["current_health"] -= damage

    print("You parry your foe's attack and hit them for " +str(damage)+" damage!")

def monster_parry_player(monster):
    global player

    damage = monster["stat_dict"]["DEX"]

    player["current_health"] -= damage

    print("Your foe parrys your attack and hits you for " +str(damage)+" damage!")

def process_combat_actions(player_action,monster_action,monster,skip):
    global player
    print("")
    if player_action != "skipped":
        player_animations = player["weapon"]["animations"][player_action]
    
    if monster_action != "skipped":
        monster_animations = monster["weapon"]["animations"][monster_action]

    if skip == "player":
        print("You are left prone from missing your last attack!")
    else:
        print(player_animations[randint(0,len(player_animations)-1)])
        

    if skip == "monster":
        print("Your for is left prone from missing their last attack!")
    else:
         print(monster_animations[randint(0,len(monster_animations)-1)])


    if player_action == "light attack":
        if monster_action != "parry":
            player_attack_monster("light",monster)
            print("")
        else:
            monster_parry_player(monster)
            return ""

    if player_action == "heavy attack":
        if monster_action != "dodge":
            player_attack_monster("heavy",monster)
            print("")
        else:
            print("Your attack is dodged!")
            print("")
            return "player"

    if monster_action == "light attack":
        if player_action != "parry":
            monster_attack_player("light",monster)
            print("")
        else:
            player_parry_monster(monster)
            print("")
            return ""

    if monster_action == "heavy attack":
        if player_action != "dodge":
            monster_attack_player("heavy",monster)
            print("")
        else:
            print("You dodge the incoming attack!")
            print("")
            return "monster"

    return ""

def encounter_loop():
    global current_room
    global player

    skip_actor = ""
    player_action = ""
    monster_action = ""

    

    defeated_monsters = []

    

    print("_________________________")
    print("")
    print(current_room["enter_encounter_desc"])

    current_monster = current_room["monster_list"][0]

    while len(current_room["monster_list"]) > 0 and player["current_health"] > 0:
        print_combat_summary(current_room["monster_list"],defeated_monsters,current_monster)
        
        if skip_actor != "player":
            player_action = get_player_action()    
        else:
            player_action = "skipped"
        
        if skip_actor != "monster":
            monster_action = get_monster_action(current_monster,skip_actor)
        else:
            monster_action = "skipped"

        skip_actor = process_combat_actions(player_action,monster_action,current_monster,skip_actor)

        if current_monster["current_health"] <= 0:
            current_room["monster_list"].remove(current_monster)
            defeated_monsters.append(current_monster)
            print(current_monster["name"] + " was defeated")
            if len(current_room["monster_list"]) > 0:
                current_monster = current_room["monster_list"][0]
        print("_________________________")


    if player["current_health"] <= 0:
        player_death()

    else:

        calculate_encounter_exp(defeated_monsters)

        current_room["items"].extend(generate_loot(defeated_monsters))

        print(current_room["leave_encounter_desc"])

#Room Loop Function__________
def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    item_list = ""
    first_item = True

    for item in items:
        if not(item["hidden"]): 
            if first_item:
                first_item = False
            else:
                item_list += ", "
            item_list += item["name"]
    
    return item_list

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    item_list = list_of_items(room["items"])
    
    if len(item_list) > 0:
        print("")
        print("There is " + item_list + " here.")
        print()

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    item_list = ""
    first_item = True

    for item in items:
        if not(item["hidden"]): 
            if first_item:
                first_item = False
            else:
                item_list += ", "
            item_list += item["name"]
    
    if len(item_list) > 0:
        print("You have " + item_list +".")
        print()

def print_inventory_list(items):
    global player
    items_array = []
    equippable = []
    useable = []
    other = []
    print("_________________________")
    print("INVENTORY:")
    print("")
    print('You have ' + str(player["gold"]) + ' gold.')
    print()




    for item in items:
        if item["hidden"] == False:
            if item["item_type"] == "weapon" or item["item_type"] == "armour":
                equippable.append(items.index(item))
            elif item["item_type"] == "healing":
                useable.append(items.index(item))
            else:
                other.append(items.index(item))

    i = 0

    if len(equippable) > 0:
        print("")
        print('You can use the following commands: [EQUIP],[USE],[LOOK],[DROP] using the item numbers:')
        print("e.g. 'drop 1' to drop item 1. (Note: '(equipable)' and '(usable)' show where their respective commands are appropriate")
        print("")
        for item_index in equippable:
            if items[item_index]['item_type'] == 'armour':
                print('[' +  str(i+1) + '] ' + items[item_index]['name'] + ' (equippable - Req STR: ' + str(items[item_index]['STR_req']) + ')')
            else:
                print('[' +  str(i+1) + '] ' + items[item_index]['name'] + ' (equippable)')
            items_array.append(item_index)
            i += 1
        print()
    if len(useable) > 0:
        for item_index in useable:
            print('[' +  str(i+1) + '] ' + items[item_index]['name'] + ' (useable)')
            items_array.append(item_index)
            i += 1
        print()
    if len(other) > 0:
        for item_index in other:
            print('[' +  str(i+1) + '] ' + items[item_index]['name'])
            items_array.append(item_index)
            i += 1  
        print()
    if len(items_array) == 0:
        print('Your inventory is empty.')
    print('EXIT or "" (no input) to return to room view.')

    return items_array

def print_summary():
    global player

    if 'name' in player['weapon']:
        weapon_stats = player['weapon']['stat_dict']
        ext_str = weapon_stats['STR']
        ext_dex = weapon_stats['DEX']
        ext_int = weapon_stats['INT']
        ext_con = weapon_stats['CON']
    else:
        ext_str = 0
        ext_dex = 0
        ext_int = 0
        ext_con = 0

    print('------')
    print('STATS')
    print('------')
    print('Strength: ' + str(player['stat_dict']['STR'] + ext_str))
    print('Dexterity: ' + str(player['stat_dict']['DEX'] + ext_dex))
    print('Intelligence: ' + str(player['stat_dict']['INT'] + ext_int))
    print('Constitution: ' + str(player['stat_dict']['CON'] + ext_con))
    print()
    print('------')
    print('EQUPPED ITEMS:')
    print('------')
    if 'name' in player['weapon']:
        print('Weapon: ' + player['weapon']['name'])
    else:
        print('Weapon: NONE')
    if 'name' in player['armour']:
        print('Armour: ' + player['armour']['name'])
    else:
        print('Armour: NONE')
    print()
    print('------')
    print('HEALTH: ' + str(player['current_health']))
    print('------')
    print()
    print("hit enter to return to room view.")
    input("")

def print_room(room):
    # Display room name
    print()
    print(" - "+room["name"].upper()+" - ")
    print()
    # Display room description
    print("__")
    print("")
    print(room["description"])

    print("__")
    print_room_items(room)

def exit_leads_to(room,direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    
    if direction in room["exit_action_desc"]:
        return room["exit_action_desc"][direction]
    else:
        return ""

def print_exit(direction, leads_to):
   
    print(direction.upper() +" "+ leads_to)


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print


    """
    global current_room
    print("You can:")
    print("")
    # Iterate over available exits
    for direction in exits:
        # print the exit name and where it leads to
        if is_valid_exit(direction,current_room):
            print_exit(direction, exit_leads_to(current_room,direction))
    
    item_count = 0
    for item in room_items:
        if item_count == 0:
            print("")
        item_count += 1
        print("[TAKE] "+str(item_count)+ " to take " + item["name"] + ".")

    if len(current_room['vendor']) == 1:
        print("")
        print('[TRADE] to buy or sell items from ' + current_room['vendor'][0]['name'] + '.')
    print("")
    print('[SUMMARY or S] to view your characters euippeed items and statistics.')
    print("[INVENTORY or I] to open your inventory.")
    print("")
    print("What do you want to do?")



def is_valid_exit(chosen_exit,room):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    """
    global player
    if chosen_exit.lower() in room["exits"]:
        if chosen_exit.lower() in room["exit_req_inv"]:
            for itemname in room["exit_req_inv"][chosen_exit.lower()]:
                if not(check_player_has_item(player,itemname)):
                     return False
        if chosen_exit.lower() in room["exit_req_equ"]:
            for itemname in room["exit_req_equ"][chosen_exit.lower()]:
                if not(check_player_equipped_item(player,itemname)):
                    return False
        
        if chosen_exit.lower() in room["exit_req_stat"]:
            for statstring in room["exit_req_equ"][chosen_exit.lower()]:
                statreq = statstring.split(',')
                if not(check_player_has_stat(player,statreq[0],statreq[1])):
                    return False
        
        return True
    else:
        return False

def execute_godmode():
    global god_mode
    
    if god_mode:
        god_mode = False
        print("")
        print("God mode off!")
    else:
        print("")
        print("Enter Password:")
        god_code = getpass(">")

        if god_code == "kirill":
            print("")
            print("God mode on")
            print("You can now use:")
            print("[GODMODE TELEPORT]")
            god_mode = True
        else:
            print("")
            print("You are unworthy!")
    

      



def execute_teleport():
      global previous_room
      global current_room
      global current_stage

      temp_stage_store = current_stage

      stage_key = ""
      room_key = ""

      print("")
      print("Teleport:")
      print("Enter the key of the stage you wish to go to.")
      print("Hit enter (no input) for current stage")
      stage_key = input(">")
      print("")
      print("Enter the key of the room you wish to go to.")
      print("Hit enter (no input) for current room")
      print("If you are changing stage, enter no input to go to 'first room'")
      room_key = input(">")
      
      if stage_key != "":
          if stage_key in game["stages"]:
              current_stage = game["stages"][stage_key]
              print("")
              print("Stage found")

          else:
              print("")
              print("no stage with that key found, you will stay in current stage")
      else:
          print("")
          print("Staying in current stage")

      if room_key in current_stage:
        previous_room = current_room
        current_room = current_stage[room_key]
        print("")
        print("Room found")
                
      else:
        print("")
        print("Room key not found.")
        if stage_key != "":
            if game["stages"][stage_key] != temp_stage_store:
                print("")
                print("Room will be set to 'first room' of "+ stage_key)
                current_stage = game["stages"][stage_key]
                previous_room = current_room
                current_room = current_stage["first room"]
            else:
                print("")
                print("No movement will be made")
        else:
                print("")
                print("No movement will be made")
        
        

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global previous_room
    global current_room
   
    
    direction = direction.lower()
    if is_valid_exit(direction,current_room):
        print(current_room["exits"][direction])
        previous_room = current_room
        current_room = move(current_room["exits"],direction)
        
    else:
        print("You cannot go there.")

def execute_take(item_index):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    global current_room
    global player_max_carry

    visible_items = []

    for item in current_room["items"]:
        if item["hidden"] == False:
            visible_items.append(item)
    if len(visible_items) > 0: 
        try:
            index = (int(item_index) -1)

            item = visible_items[index]
            if (get_inventory_mass(player) + item["mass"]) <= player["max_carry"]:
                current_room["items"].remove(item)
                player["inventory"].append(item)
            else:
                print("You are over-encumbered, you will need to drop an item")
        except:
            print("Not a valid item number.")

            
    else:
        print("There is nothing to take here")

def execute_drop(item_index):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    global player
    visible_items = []

    for item in player["inventory"]:
        if item["hidden"] == False:
            visible_items.append(item)
    
    if len(visible_items) > 0: 
        try:
            index = int(item_index) -1
            item = visible_items[index]
            current_room["items"].append(item)
            player["inventory"].remove(item)
        except:
            print("Not a valid item number.")  
    else:
        print("")
        print("You have nothing to drop.")
 
def execute_equip(item_index):
    global player
    visible_items = []

    for item in player["inventory"]:
        #if item["hidden"] == False and (item["type"] == "weapon" or item["type"] == "weapon"):
        if item["hidden"] == False:
            visible_items.append(item)
    
    if len(visible_items) > 0: 
        try:
            index = int(item_index)-1
            item = visible_items[index]
            equip_item_result = equip_item(player,item)
            if equip_item_result == 0:
                print("You can't equip that item")
            if equip_item_result == 2:
                print("You do not meet the requirements for that item")
        except:
            print("Not a valid item number.")  
    else:
        print("You have nothing to equip.")

def execute_look(item_index):
    global player
    visible_items = []

    for item in player["inventory"]:
        #if item["hidden"] == False and (item["type"] == "weapon" or item["type"] == "weapon"):
        if item["hidden"] == False:
            visible_items.append(item)

    if len(visible_items) > 0:
        try:
            index = int(item_index) - 1
            item = visible_items[index]
            print('------')
            if item['item_type'] == 'weapon':
                print('Name: ' + str(item['name']))
                print('Description: ' + str(item['description']))
                print('Mass: ' + str(item['mass']))
                print()
                print('Strength: +' + str(item['stat_dict']['STR']))
                print('Dexterity: +' + str(item['stat_dict']['DEX']))
                print('Intelligence: +' + str(item['stat_dict']['INT']))
                print('Constitution: ' + str(item['stat_dict']['CON']))
                print()
                print('Min-Max Damage: ' + str(item['min_dmg']) + '-' + str(item['max_dmg']))
            elif item['item_type'] == 'armour':
                print('Name: ' + str(item['name']))
                print('Description: ' + str(item['description']))
                print('Mass: ' + str(item['mass']))
                print()
                print('Damage Reduction: ' + str(item['armour value']))
                print('Strength Required:' + str(item['STR_req']))
            elif item['item_type'] == 'healing':
                print('Name: ' + str(item['name']))
                print('Description: ' + str(item['description']))
                print('Mass: ' + str(item['mass']))
                print()
                print('Heal Value: ' + str(item['heal_value']))
            else:
                print('Name: ' + str(item['name']))
                print('Description: ' + str(item['description']))
                print('Mass: ' + str(item['mass'])) 
            print('------')
            print()               

        except:
            print("Not a valid item number.")
    else:
        print("You have nothing to look at.")

def execute_use(item_index):
    global player
    visible_items = []

    for item in player["inventory"]:
        ##if item["hidden"] == False and (item["type"] == "weapon" or item["type"] == "weapon"):
        if item["hidden"] == False:
            visible_items.append(item)
    
    if len(visible_items) > 0: 
        try:
            index = int(item_index) - 1
            item = visible_items[index]
            if item['item_type'] == 'healing':
                heal_player(player,item['heal_value'])
                print(item['use_description'])
            else:
                print('You cannot use this item.')
        except:
            print("Not a valid item number.")  
    else:
        print("You have nothing to use.")

def execute_inventory(items):
    exit = False
    while exit == False:
        exit = inventory_menu(items)
              
def execute_command(input):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    #Function now takes the entire input string before the split by spaces

    global current_room

    if input == "":
        return
    #input string is checked for being one of the exit commands or a single word command
    if is_valid_exit(input,current_room):
        execute_go(input)
    
    elif input == "godmode":
        execute_godmode()
    
    elif input == "godmode teleport":
        if god_mode:
            execute_teleport()
        else:
            print("")
            print("Not a recognised command")


        
    elif input == "inventory" or input == "i":
        execute_inventory(player["inventory"])

    elif input == 'summary' or input == 's':
        print_summary()

    elif input == "trade":
        if len(current_room['vendor']) == 1:
            execute_trade(current_room['vendor'][0])
        else:
            print('There is no one to trade with here.')
    elif input == "buy":
        if len(current_room['vendor']) == 1:
            execute_buy(current_room['vendor'][0], 0)
        else:
            print('There is no one to trade with in this room.')
    elif input == "sell":
        if len(current_room['vendor']) == 1:
            execute_sell(current_room['vendor'][0])
        else:
            print('There is no one to trade with in this room.')     
    else:    
        #if not an exit command or single word command the input is split as before and checked for [verb,noun] structure.
        command = normalise_input(input)
        if len(command) > 1:
            if command[0] == "take": 
                execute_take(command[1])

            elif command[0] == "drop":
                execute_drop(command[1])

            elif command[0] == "equip":
                execute_equip(command[1])

            elif command[0] == "look":
                execute_look(command[1])

            elif command[0] == "use":
                execute_use(command[1])

            elif command[0] == "buy":
                if len(current_room['vendor']) == 1:
                    if int(command[2]) == 0:
                        if len(current_room['vendor'][0]['stock_items']) > 0:
                            execute_buy_item(command[1], 0)
                        else:
                            print('This vendor is not selling any items.')
                    if int(command[2]) == 1:
                        if len(current_room['vendor'][0]['acquired_items']) > 0:
                            execute_buy_item(command[1], 1)
                        else:
                            print('This vendor is not selling any items.')
                else:
                    print('There is no one to trade with in this room.')

            elif command[0] == "inspect":
                if len(current_room['vendor']) == 1:
                    if int(command[2]) == 0:
                        if len(current_room['vendor'][0]['stock_items']) > 0:
                            execute_inspect_item(command[1], 0)
                        else:
                            print('This vendor is not selling any items.')
                    if int(command[2]) == 1:
                        if len(current_room['vendor'][0]['acquired_items']) > 0:
                            execute_inspect_item(command[1], 1)
                        else:
                            print('This vendor has not previously purchased items.')
                else:
                    print('There is no one to trade with in this room.')

            elif command[0] == "sell":
                if len(current_room['vendor']) == 1:
                    items_index_array = []
                    i = 0
                    if len(player['inventory']) > 0:
                        for item in player['inventory']:
                            if item["hidden"] == False:
                                items_index_array.append(i)
                            i += 1
                        if len(items_index_array) >= int(command[1]) and int(command[1]) > -1:
                            execute_sell_item(items_index_array, command[1])
                    else:
                        print('You do not have any items to sell')
                else:
                    print('There is no one to trade with in this room.')

        else:
            if len(command) == 1:
                if command[0] == "take" or command[0] == "take" or command[0] == "use" or command[0] == "look" or command[0] == "drop":
                    print("")
                    print("You must follow an item command with a number e.g. 'drop 1'")
                else:
                    print("")
                    print("Not a recognised command")
def process_inventory_input(items_array):
    user_input = input('> ')
    clean_user_input = remove_punct(user_input)
    input_array = clean_user_input.split()
    exit = False
    if clean_user_input != '':
        if input_array[0] == 'look' or input_array[0] == 'equip' or input_array[0] == 'drop' or input_array[0] == 'use':
            if len(input_array) == 2 and input_array[1].isdigit() and int(input_array[1]) <= len(items_array) and int(input_array[1]) > 0:
                execute_command(input_array[0] + ' ' + str(items_array[int(input_array[1])-1]))
            elif len(input_array) == 1:
                print(input_array[0].capitalize() + ' what?')
            elif len(input_array) == 2:
                print('There was an error in your item number.')
        elif input_array[0] == 'exit' or input_array[0] == '':
            exit = True
        else:
            print('This make no sense.')
    else:
        exit = True

    return exit

def inventory_menu(items):
    items_array = print_inventory_list(items)

    exit = process_inventory_input(items_array)

    return exit

def trade_menu(vendor):
    global player
    print("")
    print("_________________________")
    print("")
    print('------')
    print('You are talking to ' + vendor['name'])
    print(vendor['description'])
    print('------')
    print()
    print('You have ' + str(player['gold']) + ' gold.')
    print()
    print('You can:')
    print('BUY items from the vendor.')
    print('SELL item to the vendor.')
    print('EXIT to exit.')

def trade_input():
    print("")
    user_input = input('> ')
    clean_user_input = remove_punct(user_input)
    input_array = clean_user_input.split()
    return input_array

def execute_trade(vendor):
    exit = False
    while exit == False:
        trade_menu(vendor)
        user_input = trade_input()
        if len(user_input) == 1:
            if user_input[0] == 'buy' or user_input[0] == 'sell':
                execute_command(user_input[0])
            elif user_input[0] == 'exit':
                exit = True
            else:
                print('This makes no sense.')
        else:
            print('This makes no sense.')

def buy_menu(vendor, repurchase):
    print("")
    print("_________________________")
    print("")
    print('You have ' + str(player['gold']) + ' gold.')
    print()
    if repurchase == 0:
        print("")
        print('You can [BUY] or [INSPECT] + Item Number to interact with an item. \n [REPURCHASE] to view items that were previously purchased by the vendor. \n [EXIT] to stop buying.')
        items = vendor['stock_items']
    else:
        print("")
        print("You can [BUY] or [INSPECT] + Item Number to interact with an item. \n [PURCHASE] to return the merchant's standard stock. \n [EXIT] to stop buying.")
        items = vendor['acquired_items']
    if len(items) > 0:
        print("")
        print('Items for sale:')
        for index,item in enumerate(items):
            print('[' + str(index+1) + '] ' + item['name'] + ' (' + str(item['buy_value']) + ' gold)')
    else:
        print("")
        print('The vendor has no items for sale.')

def execute_buy_item(input, repurchase):
    if repurchase == 0:
        items = current_room['vendor'][0]['stock_items']
    else:
        items = current_room['vendor'][0]['acquired_items']
    input = int(input) - 1
    if len(items) > input:
        if player['gold'] >= items[input]['buy_value']:
            print("")
            print("__")
            print("")
            print("You hand over the gold and receive:")
            print(items[input]["name"])
            print("__")
            player['gold'] -= items[input]['buy_value']
            player['inventory'].append(items[input])
            items.remove(items[input])
            
        else:
            print("")
            print('You do not have enough gold to purchase this item.')
    else:
        print('This item does not exist.')

def execute_inspect_item(input, repurchase):
    if repurchase == 0:
        items = current_room['vendor'][0]['stock_items']
    else:
        items = current_room['vendor'][0]['acquired_items']
    input = int(input) - 1
    if len(items) > input:
        item = items[input]
        print('------')
        if item['item_type'] == 'weapon':
            print('Name: ' + str(item['name']))
            print('Description: ' + str(item['description']))
            print('Mass: ' + str(item['mass']))
            print()
            print('Strength: +' + str(item['stat_dict']['STR']))
            print('Dexterity: +' + str(item['stat_dict']['DEX']))
            print('Intelligence: +' + str(item['stat_dict']['INT']))
            print('Constitution: ' + str(item['stat_dict']['CON']))
            print()
            print('Min-Max Damage: ' + str(item['min_dmg']) + '-' + str(item['max_dmg']))
        elif item['item_type'] == 'armour':
            print('Name: ' + str(item['name']))
            print('Description: ' + str(item['description']))
            print('Mass: ' + str(item['mass']))
            print()
            print('Damage Reduction: ' + str(item['armour value']))
            print('Strength Required:' + str(item['STR_req']))
        elif item['item_type'] == 'healing':
            print('Name: ' + str(item['name']))
            print('Description: ' + str(item['description']))
            print('Mass: ' + str(item['mass']))
            print()
            print('Heal Value: ' + str(item['heal_value']))
        else:
            print('Name: ' + str(item['name']))
            print('Description: ' + str(item['description']))
            print('Mass: ' + str(item['mass'])) 
        print('------')
        print()               
    else:
        print('This item does not exist.')

def execute_buy(vendor, repurchase):
    exit = False
    while exit == False:
        if repurchase == 0:
            buy_menu(vendor, 0)
        else:
            buy_menu(vendor, 1)
        user_input = trade_input()
        if len(user_input) == 2:
            if user_input[1].isdigit() and int(user_input[1]) <= len(vendor['stock_items']):
                if user_input[0] == 'buy' or user_input[0] == 'inspect':
                    execute_command(user_input[0] + ' ' + str(user_input[1]) + ' ' + str(repurchase))
                else:
                    print('This makes no sense.')
            else:
                print('This makes no sense.')
        elif len(user_input) == 1:
            if repurchase == 0:
                if user_input[0] == 'repurchase':
                    execute_buy(vendor, 1)
                elif user_input[0] == 'exit':
                    exit = True
                else:
                    print('This makes no sense.')
            else:
                if user_input[0] == 'purchase':
                    execute_buy(vendor, 0)
                elif user_input[0] == 'exit':
                    exit = True
                else:
                    print('This makes no sense.')                
        else:
            print('This makes no sense.')

def sell_menu(vendor, items_index_array):
    print("")
    print("_________________________")
    print("")
    print('You have ' + str(player['gold']) + ' gold.')
    print()
    print('You can use [SELL] or [LOOK] + Item Number to interact with an ite.\n [EXIT] to stop selling.')
    indices = items_index_array
    if len(indices) > 0:
        print('Items you can sell:')
        for index_array, index_item in enumerate(indices):
            item = player['inventory'][index_item]
            print('[' + str(index_array+1) + '] ' + item['name'] + ' (' + str(item['sell_value']) + ' golds)')
    else:
        print('You have no items to sell.')

def execute_sell_item(items, input):
    #input = int(input) - 1
    input = int(input)
    item = player['inventory'][items[input]]
    if len(items) > input:
        if item['sell_value'] > 0:
            player['gold'] += item['sell_value']
            player['inventory'].remove(item)
            current_room['vendor'][0]['acquired_items'].append(item)
        else:
            print("__")
            print("")
            print('"I am not interested in buying this item."')
            print("__")
    else:
        print("")
        print('This item does not exist.')

def execute_sell(vendor):
    exit = False
    while exit == False:
        i = 0
        items_index_array = []
        if len(player['inventory']) > 0:
            for item in player['inventory']:
                if not item["hidden"]:
                    items_index_array.append(i)
                i += 1   

        sell_menu(vendor, items_index_array)
        user_input = trade_input()
        if len(user_input) == 2:
            if user_input[1].isdigit() and int(user_input[1]) < len(items_index_array):
                if user_input[0] == 'sell' or user_input[0] == 'look':
                    execute_command(user_input[0] + ' ' + str(items_index_array[int(user_input[1])-1]))
                else:
                    print('This makes no sense.')
            else:
                print('This makes no sense.')
        elif len(user_input) == 1:
            if user_input[0] == 'exit':
                exit = True
            else:
                print('This makes no sense.')                
        else:
            print('This makes no sense.')

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    #normalised_user_input = normalise_input(user_input)

    #REMOVE PUNCTUATION AND WHITE SPACE ONLY
    clean_user_input = remove_punct(user_input)

    return clean_user_input

def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return current_stage[exits[direction]]

def main():
    no_quit = True
    game = False
    menu_check = ""
    while no_quit:
        menu_check = main_menu(game)
        if menu_check == "exit":
            no_quit = False
        elif menu_check == "game":
            game = True
        
        if game == True:
            game_loop()


    
def game_loop():

    initialise_game()
    
        


    # Main game loop
    while True:
        
        enter_room_check()

        

        # Display game status (room description, inventory etc.)
        print("_________________________")
        print_room(current_room)

        """After printing the name and description of the room the engine checks for the with name "exit game token". 
        If it finds it, the main game loop shoud be exited and the game should return to the game engine main menu.
        Thus the final room the player enters (the one that has the auto give "exit game token") will display it's name and description ( perhaps a congratulations message) and the game will quit
        
        """
        if check_for_victory():
            break

        print_inventory_items(player["inventory"])

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], player["inventory"])

        # Execute the player's command
        execute_command(command)
        
       
        #place holder message to be replaced with a return to the main menu
    print("Game quit")

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
    
