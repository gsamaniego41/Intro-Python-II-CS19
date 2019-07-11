# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room, inventory=[]):
        self.name = name
        self.current_room = starting_room
        self.inventory = inventory

    def move_player(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print('\n==================================')
            print(
                f'{self.current_room.name}.\n{self.current_room.desc}\n\nItems in this room:\n{self.current_room.items}\n==================================\n')
            print(f'Inventory: {self.inventory}')
        else:
            print('\n*******************\n*  No room there  *\n*******************')

    def item_action(self, action, item):
        if action == 'take':
            if item in self.current_room.items:
                self.inventory.append(item)
                print(f'==== Acquired {item} ====')
            else:
                print('Item does not exist')
        elif action == 'drop':
            self.inventory.remove(item)
            print(f'Discarded {item}')
