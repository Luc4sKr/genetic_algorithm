import random

from genetic.individual import Individual
from genetic.population import Population

class TournamentSelection:
    def __init__(self, tournament_size: int = 3):
        self.tournament_size = tournament_size

    def select(self, population: Population) -> Individual:
        candidates = random.sample(
            population.individuals,
            k=min(self.tournament_size, len(population.individuals))
        )

        return min(candidates, key=lambda individual: individual.cost)