class calculator:
    """On decouvre les magic method pour arithmetique"""
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object):
        i = 0
        while i < len(self.vector):
            self.vector[i] += object
            i += 1
        print(self.vector)

    def __sub__(self, object):
        i = 0
        while i < len(self.vector):
            self.vector[i] -= object
            i += 1
        print(self.vector)

    def __mul__(self, object) -> None:
        i = 0
        while i < len(self.vector):
            self.vector[i] *= object
            i += 1
        print(self.vector)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: Division by zero")
            return
        i = 0
        while i < len(self.vector):
            self.vector[i] /= object
            i += 1
        print(self.vector)
