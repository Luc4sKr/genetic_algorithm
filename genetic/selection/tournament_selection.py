import random

from genetic.individual import Individual
from genetic.population import Population
from genetic.selection.selection import Selection

class TournamentSelection(Selection):
    def __init__(self, tournament_size: int = 3):
        self.tournament_size = tournament_size

    def select(self, population: Population) -> Individual:
        '''Seleciona um indivíduo através de um torneio entre indivíduos aleatórios da população. 
        O indivíduo com o menor custo é selecionado como vencedor do torneio.'''
        
        candidates = random.sample(
            population.individuals,
            k=min(self.tournament_size, len(population.individuals))
        )

        return min(candidates, key=lambda individual: individual.cost)