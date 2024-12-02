from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """L'heredité c'est compliqué #Medicine
    Thanks to the fixs we dont have to
    worry about the diamond problem anymore
    exo obsolète"""
    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
