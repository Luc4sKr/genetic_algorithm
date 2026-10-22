import random

from problem.tsp import TSP
from genetic.individual import Individual
        
class Population:
    def __init__(self, population_size: int, chromosome_length: int):
        self.individuals = []
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        
    def generate_random_population(self):
        self.individuals = [
            Individual(random.sample(range(self.chromosome_length), self.chromosome_length))
            for _ in range(self.population_size)
        ]
        
    def evaluate(self, problem: TSP) -> Individual:
        best = None
        best_cost = float("inf")
        
        for individual in self.individuals:
            cost = problem.calculate_tour_distance(individual.chromosome)
            individual.cost = cost
            if cost < best_cost:
                best_cost = cost
                best = individual

        return best

    def sort_by_cost(self):
        self.individuals.sort(key=lambda ind: ind.cost)