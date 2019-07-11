# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def move_player(self, direction):
        if getattr(self.room, f'{direction}_to') is not None:
            self.room = getattr(self.room, f'{direction}_to')
        else:
            print('please enter n, s, e, w, or q')
