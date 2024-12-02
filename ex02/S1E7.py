from S1E9 import Character


class Baratheon(Character):
    "Class specific to Baratheon family"
    def __init__(self, first_name, is_alive=True):
        "Jconnais pas la serie mais je crois son nom c'est Baratheon"
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


class Lannister(Character):
    "Class specific to Lannister family"
    def __init__(self, first_name, is_alive=True):
        "A new Lannister has entered the game"
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
