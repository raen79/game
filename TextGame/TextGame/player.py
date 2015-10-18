#forcechange
previous_room = {}
current_room = {}
current_stage = {}

player = {
"name":"",                                                                                      # Player's name displayed in combat 
"description":"",                                                                               # Description shown when using the "LOOK" command
"stat_dict":{"STR":3,"DEX":3,"INT":3,"CON":3},                                                 # the stats of the player
"armour":{},                                                                                    # (An armour dictionary variable e.g. "armour":leather_001) The dictionary for the equiped armour
"weapon":{},                                                                                    # (A weapon dictionary variable e.g. "weapon":sword_001) The dictionary for the equiped weapon
"current_health":15,                                                                             # Current health of the player.
"max_health":15,                                                                                 # This will be calculated and updated based on the player's constitution.
"current_combat_mod":0,                                                                         # Calculated by the engine at the begining of combat
"level":1,                                                                                      
"exp":0,                                                                                        
"inventory":[],                                                                                  # A list of item dictionaries representing the player's inventory  
"max_carry":0,
"gold":0
}



def calculate_exp_gain(monster_lvl):
    exp_mod =(0.4 ** player["level"]) + ((monster_lvl - player["level"]) * 0.005)
    return calculate_next_level_req() * exp_mod

#handles the gain in exp, and the level up process
def player_gain_exp(exp):
    if exp > 0:
        player["exp"] += exp
        if player["exp"] >= calculate_next_level_req():
            player["level"] += 1
            render_level_up_menu()
            calculate_working_stats()
            player["current_health"] = player["max_health"]

def calculate_next_level_req():
    return (2**(player["level"]-1))*100

def render_level_up_menu():
    points_per_level = 3
    
    stat_increase = {"STR":0,"DEX":0,"INT":0,"CON":0}
    print("_________________________")
    print("")
    print("Congratulations you have leveled up!")
    print("You have " + str(points_per_level) +"stat points to spend.")
    print("Current Stats:")
    for stat in player["stat_dict"]:
        print(stat + ": " + str(player["stat_dict"][stat]))
    
    points_available = True

    while points_available:
        for point in range(1,(points_per_level + 1)):
            need_input = True      
            while need_input:
                stat_input = str(input("Where would you like to spend point "+str(point)+" ? (enter STR,DEX,INT or CON)")).upper()
                if stat_input in stat_increase:
                    stat_increase[stat_input] += 1
                    need_input = False
                else:
                    print("Invalid Input")

        for stat in player["stat_dict"]:
            print(stat + ":     " + str(player["stat_dict"][stat]) + "   +"+str(stat_increase[stat])+"    new value:"+ str(player["stat_dict"][stat] + stat_increase[stat]))
        print("")
        need_input = True      
        while need_input:
            input_confirm = str(input("Are you happy with these choices? (Yes or No)")).upper() 
            if input_confirm == "YES":
                for stat in player["stat_dict"]:
                    player["stat_dict"][stat] += stat_increase[stat]
                
                need_input = False
                points_available = False
            elif input_confirm == "NO":
                need_input = False
            else:
                print("Invalid Input")
    print("_________________________")

def heal_player(heal_amount):
    if heal_amount > 0:
        missing_health = player["max_health"] - player["current_health"]
        if missing_health >= heal_amount:
             player["current_health"] += heal_amount
        else:
             player["current_health"] += missing_health

def damage_player(dmg_amount):
    if dmg_amount > 0:
        
        if player["current_health"]  >= dmg_amount:
             player["current_health"] -= dmg_amount
        else:
             player["current_health"] = 0
          
def equip_item(item):
    if item in player["inventory"]:
        if item["item_type"] == "weapon":
            player["weapon"] = item
            player["inventory"].remove(item)
            calculate_working_stats()
            return True
        if item["item_type"] == "armour":
            player["armour"] = item
            player["inventory"].remove(item)
            calculate_working_stats()
            return True
    
    return False

def calculate_working_stats():
    player["max_health"] = calculate_max_health()
    player["current_combat_mod"] = calculate_combat_mod()
    player["max_carry"] = calculate_max_carry()

def calculate_max_health():
    health_per_con = 5
    return health_per_con * player["stat_dict"]["CON"]

def calculate_combat_mod():
    combat_stat = 0
    weapon_value = 0

    combat_stat_key = get_player_combat_stat()

    base_value = player["stat_dict"][combat_stat_key]

    equiped_weapon = player["weapon"]
    if len(equiped_weapon) > 0:
        weapon_value = equiped_weapon["stat_dict"][combat_stat_key]

    combat_stat = base_value + weapon_value
    return combat_stat

def calculate_max_carry():
    kg_per_str = 5
    return kg_per_str * player["stat_dict"]["STR"]

def get_inventory_mass():
    TotalMass = 0.0
    for item in player["inventory"]:
        TotalMass += item["mass"]
    return TotalMass

def get_player_combat_stat():
    if check_player_has_item("fighter path"):
        return "STR"
    if check_player_has_item("rogue path"):
        return "DEX"
    if check_player_has_item("mage path"):
        return "INT"

    #no class chosen
    return "STR"

def check_player_has_item(item_name):
    for item in player["inventory"]:
        if item["name"].lower() == item_name.lower():
            return True
    return False

  