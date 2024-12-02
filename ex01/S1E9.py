from abc import ABC, abstractmethod


class Character(ABC):
    "ABC Class used to create new Characters"
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """New char joined the serie"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Mort mort mort"""
        if self.is_alive is True:
            self.is_alive = False

    def __str__(self):
        """On peut STR et REPR dans main class abstraite
        tres pratique encore une fois pour eviter la repetition"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        str = self.__str__()
        return str


class Stark(Character):
    "Class specific to Stark family"
    def __init__(self, first_name, is_alive=True):
        "New character of Stark family init"
        super().__init__(first_name, is_alive)
