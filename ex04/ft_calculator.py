class calculator:
    """Static methods me permettent de pas instancier
    la classe pour l'utiliser, this is very cool"""
    @staticmethod
    def dotproduct(V1: list[float], v2: list[float]) -> None:
        i = 0
        dot = 0
        while i < len(V1):
            dot += V1[i] * v2[i]
            i += 1
        print(dot)

    @staticmethod
    def add_vec(V1: list[float], v2: list[float]) -> None:
        i = 0
        new_vec = [0 for i in range(len(V1))]
        while i < len(V1):
            new_vec[i] = V1[i] + v2[i]
            i += 1
        print(new_vec)

    @staticmethod
    def sous_vec(V1: list[float], v2: list[float]) -> None:
        i = 0
        new_vec = [0 for i in range(len(V1))]
        while i < len(V1):
            new_vec[i] = V1[i] - v2[i]
            i += 1
        print(new_vec)
