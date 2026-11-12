from genetic.individual import Individual
from genetic.operators.cycle_crossover import CycleCrossover
from genetic.operators.swap_mutation import SwapMutation
from genetic.operators.crossover_pmx import CrossoverPMX
from genetic.population import Population
from genetic.selection.selection import Selection
from genetic.stagnation_criteria import StagnationCriteria
from problem.problem import Problem

class GA:
    def __init__(
        self, 
        problem: Problem, 
        population_size: int, 
        generation_size: int,
        elite_size: int,
        selection: Selection,
        stagnation_criteria: StagnationCriteria
    ):
        self.problem = problem
        self.population_size = population_size
        self.generation_size = generation_size
        self.elite_size = elite_size
        self.selection = selection
        self.stagnation_criteria = stagnation_criteria
        
        chromosome_length = len(problem.cities)
        self.population = Population(
            population_size, 
            chromosome_length
        )
        
        self.mutation = SwapMutation()
        self.crossover = CycleCrossover()
        
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
            
            child1, child2 = self.crossover.execute(parent1, parent2)
            
            self.mutation.mutate(child1)
            new_population.add_individual(child1)
            if len(new_population.individuals) < self.population_size:
                self.mutation.mutate(child2)
                new_population.add_individual(child2)
            
        self.population = new_population
        
    def print_results(self):
        print(f"population size: {self.population_size}")
        print(f"generation size: {self.generation_size}")
        print(f"cities: {len(self.problem.cities)}")
        print(f"best cost: {self.best_individual.cost}")
        print(f"best route: {self.best_individual.chromosome}")
        
    def run(self) -> list[int]:
        self.initialize()
        self.evaluate()
        
        for generation in range(self.generation_size):
            should_stop = self.stagnation_criteria.verify(self.best_individual.cost)
            if should_stop:
                print(f"Stopping at generation {generation} due to stagnation.")
                break
            
            self.next_generation()
            self.evaluate()
        
        self.print_results()
        return self.best_individual.chromosome.copy()
        
        