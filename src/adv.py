from room import Room
from player import Player
from item import Item
from item import Gold

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Axe", "A dull axe"), Gold(10)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Wand", "An old wand with strange runes" )]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Skull", "A pale white skull of some strange monster")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Key", "A bent key")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Map", "A faded map")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

newPlayer = Player("David", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def movePlayer(direction):
    direction_to = direction + "_to"

    if (selectDirection == direction):
        if(hasattr(newPlayer.current_room, direction_to)):
            newPlayer.current_room = getattr(newPlayer.current_room, direction_to)

            print(newPlayer.current_room)
          
        else: 
            print("Try somewhere else...")
    print(newPlayer.inventory)

def takeItem(item):
    # get_item = "get" + items

    if item == "pass":
        return

    # if selectItem == get_item:
    for items in newPlayer.current_room.items:
        if(items.name == item):
            print(newPlayer.current_room.items)

            newPlayer.inventory.append(items)
            newPlayer.current_room.items.remove(items)

            print(f'Inventory: {newPlayer.inventory}')
            print(f'Room in Items: {newPlayer.current_room.items}')
        else: 
            print("Item does not exist or invalid command")

    
# for items in newPlayer.current_room.items:
#     print(f'Items: {items}')
    

# print(newPlayer.current_room.items)
# print(newPlayer.current_room)

while True:
    selectItem = input("Take item: ")
    # selectDirection = input("Choose a direction: ")

    # if (selectDirection == "q"):
    #     print("Goodbye.")
    #     break

    takeItem(selectItem)
    # movePlayer(selectDirection)

   

    