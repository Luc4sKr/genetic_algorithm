import numpy as np

from models.city import City
from problem.problem import Problem

class TSP(Problem):
    def __init__(self, cities: list[City]):
        super().__init__(cities)

    def evaluate(self, chromosome: list[int]) -> float:
        total = self.distance(chromosome[-1], chromosome[0])  # aresta que fecha o ciclo
        for i in range(len(chromosome) - 1):
            total += self.distance(chromosome[i], chromosome[i + 1])
        return total
