Creating Games
=======

 - Each individual game is stored as a folder inside the **Games** folder.
 - Each folder inside of the **Games** folder contains 6 files with the
   dictionaries that make up the game:

	* **game.py**
	* **items.py**
	* **map.py**
	* **monsters.py8**
	* **player_character.py**
	* **vendors.py**

- The values intended to be inserted into each dictionary are found in the **Dictionary Template** file. Each dictionary has comments describing the value to be found in each key within the dictionaries
 

## game.py
- The **game.py** file contains the dictionaries that make up each stage of the game, titled **stageX** where x is the stage number. 
- The keys of the stage dictionaries are the names of the rooms and their content is the name of the dictionary in **map.py** that contains the details of the room

## map.py
- The **map.py** file contains the dictionaries that make up each room inside of the various stages of the game

## items.py
- The **items.py** file contains the dictionaries for all the items to be used by either the character or monsters in the game.

## monsters.py
- The **monsters.py** file contains the dictionaries for all of the monsters that may be displayed in the game

## player_character.py
- The **player_character.py** file contains the dictionary for the character that will represent the user throughout the game. Three variables are found within the files along with the dictionary, these are to be used by the engine only and are not to be modified:
	* previous_room
	* current_room
	* current_stage

## vendors.py
- The **vendors.py** file contains the dictionaries for the vendors that may be displayed in the game. When interacting with these vendors, a trade menu will be opened that will allow the user to purchase, sell, or re-purchase items.

The Engine
=======
The engine is composed of three files:
- **command_parser.py**
- **game_engine.py**
- **player.py**

## command_parser.py
The main function in this file is *normalise_input* which returns the an array composed of the words contained with any string that is fed into it. It uses the function *remove_punct* which removes any punctuation from strings that are fed into it.

## player.py
The functions in this file relate to actions that deal with modifying and understanding the status quo of the player. The main functions are displayed here:
- Experience
	- The amount of experience gained by a character after fighting a monster is defined by the *calculate_exp_gain* function.
	- The player will actually gain the experience with the *player_gain_exp* function that will also level up the player in the case that he has gained enough experience to do so
- Levelling up
	- The amount of experience needed for levelling up the player is measured by the *calculate_next_level_req* function.
	- The levelling up menu which allows the player to modify their stats is contained within the *render_level_up_menu* function.
- Health
	- The health of the player is modified with the *heal_player* and *damage_player* functions
- Equipping items
	- The function that allows a player to equip an item is named *equip_item*

## game_engine.py
This file contains most functions relating to the engine. Below is an explanation of the most important or complex aspect of the engine:
- Main loop
	- The main loop, represented by the *main* function, runs unless the user choses to exit it in the main menu. Otherwise it loads the *main_menu* which asks for the users input as to whether they want to resume or restart the current game, play the loaded game, load another game, find out more about the game, or exit it. The games are placed in the games folder.
- Menu Loop
	- The menu loop, represented by *menu* function, prints all the options available to the player at any given point in time and takes the input of the player. This loop exists in the game loop which is loaded when the game is started. The input of the player is processed by the *execute_command* function described below.
- Inventory Loop
	- The inventory loop is contained within the *execute_inventory* function. It loads the function *inventory_menu* which prints the user’s inventory using the *print_inventory_list*. The inventory items are printed in three groups, those that are equippable, useable, and others. After being printed in this order, the indices of the items are stored in said order inside of the array items_array which is then sent to the *process_inventory_input* function. It uses the ordered list of items to interpret the value of the item the user inputs and sends off the appropriate command to the *execute_command* function.
- Trade Loop
	- The trade loop contained in the function execute_trade works in the same way as the inventory loop. The difference is that the execute_trade function is a loop that allows the user to choose whether they want to buy or sell items. The *execute_buy* and *execute_sell* functions in turn are the equivalent to the execute_inventory function. The functions contained within execute_buy will often receive a value called repurchase. If repurchase is set to 0, then the user will be able to buy items that the vendor has to begin with, and if it is set to 1, then the user will be able to buy items that they had already sold to the vendor.
- Execute Commands
	- The *execute_command* function interprets any input from the player into the console and sends it to the appropriate function. If the input only has one word then the function refers to it as the variable input. If the input has more than one word then the function divides the input into an array named command by using the *normalise_input* function found in *command_parser*.

