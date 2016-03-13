class Player:
    def __init__(self, name, characters=None, current_character=0):
        self.name = name
        if characters is not None:
            self.characters = characters
        else:
            self.characters = []
        self.current_character = current_character
