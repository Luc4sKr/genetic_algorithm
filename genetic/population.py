import random

from problem.problem import Problem
from genetic.individual import Individual
        
class Population:
    def __init__(self, population_size: int, chromosome_length: int):
        self.__individuals = []
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        
    @property
    def individuals(self) -> list[Individual]:
        return self.__individuals
        
    def add_individual(self, individual: Individual):
        if len(self.__individuals) >= self.population_size:
            raise ValueError("Population is already full.")
        
        self.__individuals.append(individual)
        
    def generate_random_population(self):
        for _ in range(self.population_size):
            chromosome = random.sample(range(self.chromosome_length), self.chromosome_length)
            individual = Individual(chromosome)
            self.add_individual(individual)
            
    def generate_k_nearest_neighbor_population(self, problem: Problem, K: int):
        
        pass

    def evaluate(self, problem: Problem) -> Individual:
        best = None
        best_cost = float("inf")
        
        for individual in self.__individuals:
            cost = problem.evaluate(individual.chromosome)
            individual.cost = cost
            if cost < best_cost:
                best_cost = cost
                best = individual

        return best

    def sort_by_cost(self):
        self.__individuals.sort(key=lambda ind: ind.cost)