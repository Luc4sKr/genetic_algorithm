class Individual:

    def __init__(self, chromosome: list[int]):
        self.chromosome = chromosome
        self.cost: float | None = None
        
    def copy(self) -> Individual:
        new_individual = Individual(self.chromosome.copy())
        new_individual.cost = self.cost
        return new_individual
