class Individual:

    def __init__(self, chromosome: list[int]):
        self.chromosome = chromosome
        self.cost: float | None = None
