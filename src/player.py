# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    # def __str__(self):
        # print(self.current_room)

    def move_player(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print('\n==================================')
            print(
                f'{self.current_room.name}.\n{self.current_room.desc}\n==================================')
        else:
            print('\n*******************\n*  No room there  *\n*******************')
