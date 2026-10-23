from typing import Protocol

from genetic.population import Population
from genetic.individual import Individual

class SelectionStrategy(Protocol):
    def select(
        self,
        population: Population
    ) -> Individual:
        ...