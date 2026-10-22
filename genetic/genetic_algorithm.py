from genetic.individual import Individual
from genetic.population import Population
from problem.tsp import TSP

class GA:
    def __init__(
            self, 
            problem: TSP, 
            population_size: int, 
            generations: int
    ):
        self.problem = problem
        self.population_size = population_size
        self.generations = generations
        
        chromosome_length = len(problem.cities)
        self.population = Population(population_size, chromosome_length)
        
        self.best_individual = None
    
    def initialize(self):
        self.population.generate_random_population()
    
    def evaluate(self):
        generation_best = self.population.evaluate(self.problem)

        if self.best_individual is None or generation_best.cost < self.best_individual.cost:
            snapshot = Individual(generation_best.chromosome.copy())
            snapshot.cost = generation_best.cost
            self.best_individual = snapshot
    
    def next_generation(self):
        pass
    
    def run(self) -> list[int]:
        self.initialize()
        
        for generation in range(self.generations):
           self.evaluate()
        
        return self.best_individual.chromosome
        
        