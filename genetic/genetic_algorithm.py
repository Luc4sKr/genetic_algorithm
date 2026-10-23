from genetic.individual import Individual
from genetic.operators.swap_mutation import SwapMutation
from genetic.operators.crossover_pmx import CrossoverPMX
from genetic.population import Population
from genetic.selection.selection_strategy import SelectionStrategy
from problem.tsp import TSP

class GA:
    def __init__(
        self, 
        problem: TSP, 
        population_size: int, 
        generation_size: int,
        elite_size: int,
        selection: SelectionStrategy
    ):
        self.problem = problem
        self.population_size = population_size
        self.generation_size = generation_size
        self.elite_size = elite_size
        self.selection = selection
        
        chromosome_length = len(problem.cities)
        self.population = Population(
            population_size, 
            chromosome_length
        )
        
        self.mutation = SwapMutation()
        self.crossover = CrossoverPMX()
        
        self.best_individual = None
    
    def initialize(self):
        self.population.generate_random_population()
    
    def evaluate(self):
        generation_best = self.population.evaluate(self.problem)

        if (
            self.best_individual is None 
            or generation_best.cost < self.best_individual.cost
        ):
            snapshot = Individual(generation_best.chromosome.copy())
            snapshot.cost = generation_best.cost
            self.best_individual = snapshot
            print(f"New best individual found: {self.best_individual.cost}")
    
    def appply_elite(self, new_population: Population):
        self.population.sort_by_cost()
        for i in range(0, self.elite_size):
            new_population.add_individual(self.population.individuals[i].copy())
    
    def next_generation(self):
        new_population = Population(self.population_size, self.population.chromosome_length)
        
        self.appply_elite(new_population)
        
        while len(new_population.individuals) < self.population_size:
            parent1 = self.selection.select(self.population)
            parent2 = self.selection.select(self.population)
            
            # 1) recombine parents
            child1, child2 = self.crossover.execute(parent1.chromosome, parent2.chromosome)
            
            # 2) mutate the offspring
            child1, child2 = self.mutation.mutate(child1, child2)
            
            new_population.add_individual(Individual(child1))
            if len(new_population.individuals) < self.population_size:
                new_population.add_individual(Individual(child2))
            
        self.population = new_population
        
    def run(self) -> list[int]:
        self.initialize()
        
        for generation in range(self.generation_size):
           self.evaluate()
           self.next_generation()
           
        self.evaluate()
        
        return self.best_individual.chromosome.copy()
        
        