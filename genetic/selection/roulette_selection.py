import random

from genetic.individual import Individual
from genetic.population import Population
from genetic.selection.selection import Selection


class RouletteSelection(Selection):
    def select(self, population: Population) -> Individual:
        """Seleciona um indivíduo dando maior probabilidade a custos menores."""
        
        weights = [1.0 / individual.cost for individual in population.individuals]
        total_weight = sum(weights)
        target = random.random() * total_weight
        cumulative_weight = 0.0

        for individual, weight in zip(population.individuals, weights):
            cumulative_weight += weight
            if cumulative_weight >= target:
                return individual

        return population.individuals[-1]