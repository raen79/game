#forcechange
#!/usr/bin/python3
from random import randint
from game import *
from player import *
from command_parser import *

#General Game Functions______

def move_stage_check():
    global current_room
    if len(current_room["go_to_stage"]) > 0:
        current_stage = dh_Game["stages"][current_room["go_to_stage"]]
        current_room = current_stage["first room"]

def player_death():
    global current_room
    global previous_room
    global player
    print("you have died!!")
    current_room = previous_room

    player["current_health"] = player["max_health"]
    

def check_for_victory():

    return check_player_has_item("end game token")
        
def initialise_game():
    global current_stage
    global current_room   
    global previous_room
    
    current_stage = dh_Game["stages"][dh_Game["start_stage"]]
    current_room = current_stage[dh_Game["start_room"]]
    calculate_working_stats()
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
            total_exp_gain += calculate_exp_gain(monster["level"])
        print("You gained "+ str(total_exp_gain) +" exp from the encounter!")
        player_gain_exp(total_exp_gain)

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

    player["current_health"] -= damage

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
        print('You can: LOOK [ITEM #], EQUIP [ITEM #], or DROP [ITEM #] the following items:')
        for item_index in equippable:
            if items[item_index]['item_type'] == 'armour':
                print('[' +  str(i+1) + '] ' + items[item_index]['name'] + ' (equippable - Req STR: ' + str(items[item_index]['STR_req']) + ')')
            else:
                print('[' +  str(i+1) + '] ' + items[item_index]['name'] + ' (equippable)')
            items_array.append(item_index)
            i += 1
        print()
    if len(useable) > 0:
        print('You can: LOOK [ITEM #], USE [ITEM #], or DROP [ITEM #] the following items:')
        for item_index in useable:
            print('[' +  str(i+1) + '] ' + items[item_index]['name'] + ' (useable)')
            items_array.append(item_index)
            i += 1
        print()
    if len(other) > 0:
        print('You can: LOOK [item #], or DROP [item #] the following items:')
        for item_index in other:
            print('[' +  str(i+1) + '] ' + items[item_index]['name'])
            items_array.append(item_index)
            i += 1  
        print()
    if len(items_array) == 0:
        print('Your inventory is empty.')
    print('EXIT to exit.')

    print(items)
    print(items_array)

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

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
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
    
    return room["exit_action_desc"][direction]

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

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    global current_room
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(current_room,direction))
    
    item_count = 0
    for item in room_items:
        item_count += 1
        print("TAKE "+str(item_count)+ " to take " + item["name"] + ".")
    print('SUMMARY (or S) to view the equipped items, health, and other statistics of your character.')
    print("INVENTORY (or I) to open your inventory.")
    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    
        

    return chosen_exit.lower() in exits

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global previous_room
    global current_room
   
    
    direction = direction.lower()
    if is_valid_exit(current_room["exits"],direction):
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
            if (get_inventory_mass() + item["mass"]) <= player["max_carry"]:
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
            equip_item_result = equip_item(item)
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
                player["current_health"] += item['heal_value']
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

def execute_trade():
    print("render trade")
    #needs constructing
              
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
    if is_valid_exit(current_room["exits"],input):
        execute_go(input)
    elif input == "inventory" or input == "i":
        execute_inventory(player["inventory"])

    elif input == 'summary' or input == 's':
        print_summary()

    elif input == "trade":
                execute_trade()
    else:    
        #if not an exit command or single word command the input is split as before and checked for [verb,noun] structure.
        command = normalise_input(input)
       
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

        else:
            print("This makes no sense.")

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
        elif input_array[0] == 'exit':
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

