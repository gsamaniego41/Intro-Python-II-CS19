from room import Room
from player import Player
from item import Item

item = {
    'power': Item('Power Stone', 'Purple'),
    'space': Item('Space Stone', 'Blue'),
    'time': Item('Time Stone', 'Green'),
    'mind': Item('Mind Stone', 'Yellow'),
    'reality': Item('Reality Stone', 'Red'),
    'soul': Item('Soul Stone', 'Orange'),
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

room['treasure'].add_item(item['power'])
room['treasure'].add_item(item['space'])
room['treasure'].add_item(item['time'])
room['overlook'].add_item(item['reality'])
room['overlook'].add_item(item['soul'])
room['narrow'].add_item(item['mind'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player_name = input('Your name: ')
player = Player('player1', room['outside'], [])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# ✔ Print an error message if the movement isn't allowed.
#
# ✔ If the user enters "q", quit the game.


directions = ('n', 's', 'e', 'w')
actions = ('take', 'drop')

while True:
    room = player.current_room
    map = f'North: {room.n_to}\nSouth: {room.s_to}\nEast: {room.e_to}\nWest: {room.w_to}'
    print(map)
    cmd = input('Enter a command -> ')
    cmd = cmd.split()

    if cmd[0] in directions:
        player.move_player(cmd[0])
    elif cmd[0] in actions:
        action = cmd[0]
        item = cmd[1]
        player.item_action(action, item)
    elif cmd[0] == 'q':
        print('Thanks for playing!')
        break
    else:
        print(f'''\n**********************************
            \nPlease enter a valid command
            \nOptions: n, s, e, w, q
            \n**********************************\n''')
