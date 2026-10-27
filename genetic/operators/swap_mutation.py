import random

from genetic.individual import Individual

class SwapMutation:
    """Operador de mutação que troca dois genes aleatórios no cromossomo do indivíduo."""
    
    def mutate(self, individual: Individual) -> None:
        first, second = random.sample(range(len(individual.chromosome)), 2)
        individual.chromosome[first], individual.chromosome[second] = (
            individual.chromosome[second],
            individual.chromosome[first],
        )

