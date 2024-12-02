from abc import ABC, abstractmethod


class Character(ABC):
    "AB(tract)C Class used to create new Characters"
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """New char joined the serie"""
        self.is_alive = is_alive
        self.first_name = first_name

    def die(self):
        """Mort mort mort"""
        if self.is_alive is True:
            self.is_alive = False


class Stark(Character):
    "Class specific to Stark family"
    def __init__(self, first_name, is_alive=True):
        "New character of Stark family init"
        super().__init__(first_name, is_alive)
