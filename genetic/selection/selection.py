from typing import Protocol

from genetic.population import Population
from genetic.individual import Individual

class Selection(Protocol):
    def select(
        self,
        population: Population
    ) -> Individual:
        ...