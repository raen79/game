#forcechange


def calculate_exp_gain(player,monster_lvl):
    exp_mod =(0.4 ** player["level"]) + ((monster_lvl - player["level"]) * 0.005)
    return round(calculate_next_level_req(player,) * exp_mod)

#handles the gain in exp, and the level up process
def player_gain_exp(player,exp):
    if exp > 0:
        player["exp"] += exp
        if player["exp"] >= calculate_next_level_req(player,):
            player["level"] += 1
            render_level_up_menu(player)
            calculate_working_stats(player)
            player["current_health"] = player["max_health"]

def calculate_next_level_req(player,):
    return (2**(player["level"]-1))*100

def render_level_up_menu(player):
    points_per_level = 3
    
    stat_increase = {"STR":0,"DEX":0,"INT":0,"CON":0}
    print("_________________________")
    print("")
    print("Congratulations you have leveled up!")
    print("You have " + str(points_per_level) +" stat points to spend.")
    print("Current Stats:")
    for stat in player["stat_dict"]:
        print(stat + ": " + str(player["stat_dict"][stat]))
    print("")
    points_available = True

    while points_available:
        stat_increase = {"STR":0,"DEX":0,"INT":0,"CON":0}
        print("")
        for point in range(1,(points_per_level + 1)):
            need_input = True      
            while need_input:
                stat_input = str(input("Where would you like to spend point "+str(point)+" ? (enter STR,DEX,INT or CON)")).upper()
                if stat_input in stat_increase:
                    stat_increase[stat_input] += 1
                    need_input = False
                else:
                    print("Invalid Input")

        print("")
        for stat in player["stat_dict"]:
            print(stat + ":     " + str(player["stat_dict"][stat]) + "   +"+str(stat_increase[stat])+"    new value:"+ str(player["stat_dict"][stat] + stat_increase[stat]))
        print("")
        need_input = True      
        while need_input:
            input_confirm = str(input("Are you happy with these choices? (Yes[y] or No[n])")).upper() 
            if input_confirm == "YES" or input_confirm == "Y":
                for stat in player["stat_dict"]:
                    player["stat_dict"][stat] += stat_increase[stat]
                
                need_input = False
                points_available = False
            elif input_confirm == "NO" or input_confirm == "N":
                need_input = False
            else:
                print("Invalid Input")
    print("_________________________")

def heal_player(player,heal_amount):
    if heal_amount > 0:
        missing_health = player["max_health"] - player["current_health"]
        if missing_health >= heal_amount:
             player["current_health"] += heal_amount
        else:
             player["current_health"] += missing_health

def damage_player(player,dmg_amount):
    if dmg_amount > 0:
        
        if player["current_health"]  >= dmg_amount:
             player["current_health"] -= dmg_amount
        else:
             player["current_health"] = 0
          
def equip_item(player,item):
    """
    This function is used to equip the player with the item (dictionary) passed to it.
    
    The function will return the following results:
    0 - The item is not equipable
    1 - The item was equipped
    2 - The player does not meet the requirements to equip the item. 
    """
    

    if item in player["inventory"]:
        if item["item_type"] == "weapon":
            
            #Place current weapon in to inventory
            if len(player["weapon"]) >0:
                player["inventory"].append(player["weapon"])
            
            #Take weapon from inventory and place in the player weapon slot
            player["weapon"] = item
            player["inventory"].remove(item)
            
            #recalculate stats
            calculate_working_stats(player)

            return 1
        if item["item_type"] == "armour":
            if player["stat_dict"]["STR"] >= item["STR_req"]:
                #Place current armour in to inventory
                if len(player["armour"]) >0:
                    player["inventory"].append(player["armour"])

                player["armour"] = item
                player["inventory"].remove(item)
                calculate_working_stats(player)
                return 1
            else:
                return 2
    
    return 0

def calculate_working_stats(player):
    player["max_health"] = calculate_max_health(player)
    player["current_combat_mod"] = calculate_combat_mod(player)
    player["max_carry"] = calculate_max_carry(player)

def calculate_max_health(player):
    health_per_con = 5
    return health_per_con * player["stat_dict"]["CON"] + player["base_health"]

def calculate_combat_mod(player):
    combat_stat = 0
    weapon_value = 0

    combat_stat_key = get_player_combat_stat(player)

    base_value = player["stat_dict"][combat_stat_key]

    equiped_weapon = player["weapon"]
    if len(equiped_weapon) > 0:
        weapon_value = equiped_weapon["stat_dict"][combat_stat_key]

    combat_stat = base_value + weapon_value
    return combat_stat

def calculate_max_carry(player):
    kg_per_str = 5
    return kg_per_str * player["stat_dict"]["STR"]

def get_inventory_mass(player):
  
    TotalMass = 0.0
    for item in player["inventory"]:
        TotalMass += item["mass"]

    if len(player["weapon"]) > 0:
        TotalMass += player["weapon"]["mass"] 

    if len(player["armour"]) > 0:
        TotalMass += player["armour"]["mass"]

    return TotalMass

def get_player_combat_stat(player):
    if check_player_has_item(player,"fighter path"):
        return "STR"
    if check_player_has_item(player,"rogue path"):
        return "DEX"
    if check_player_has_item(player,"mage path"):
        return "INT"

    #no class chosen
    return "STR"

def check_player_has_item(player,item_name):
    
    for item in player["inventory"]:
        if item["name"].lower() == item_name.lower():
            return True
    if len(player["weapon"]) > 0:
        if player["weapon"]["name"].lower() == item_name.lower():
            return True

    if len(player["armour"]) > 0:
        if player["armour"]["name"].lower() == item_name.lower():
            return True
    return False

def check_player_equipped_item(player,item_name):
   
    if len(player["weapon"]) > 0:
        if player["weapon"]["name"].lower() == item_name.lower():
            return True
   
    if len(player["armour"]) > 0:
        if player["armour"]["name"].lower() == item_name.lower():
            return True
    return False

def check_player_has_stat(player,stat_string,value):
    
    if player["stat_dict"][stat_string] >= value:    
        return True
    else:
        return False  