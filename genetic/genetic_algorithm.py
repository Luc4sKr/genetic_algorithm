import random

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
        survivor_size: int,
        selection: Selection,
        stagnation_criteria: StagnationCriteria
    ):
        self.problem = problem
        self.population_size = population_size
        self.generation_size = generation_size
        
        if not 1 <= survivor_size < population_size:
            raise ValueError("Survivor size must be between 1 and population size - 1.")
        
        self.survivor_size = survivor_size
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
        self.initial_population: list[Individual] = []

    def initialize(self):
        self.population.generate_random_population()

    def evaluate(self):
        generation_best = self.population.evaluate(self.problem)

        if (
            self.best_individual is None
            or generation_best.cost < self.best_individual.cost
        ):
            # Guarda uma cópia para preservar o melhor resultado da busca.
            snapshot = Individual(generation_best.chromosome.copy())
            snapshot.cost = generation_best.cost
            self.best_individual = snapshot
            print(f"New best individual found: {self.best_individual.cost}")

    def select_survivors(self) -> Population:
        candidates = Population(self.population_size, self.population.chromosome_length)
        for individual in self.population.individuals:
            candidates.add_individual(individual)

        survivors = Population(self.survivor_size, self.population.chromosome_length)
        # A roleta escolhe os sobreviventes sem selecionar o mesmo indivíduo duas vezes.
        for _ in range(self.survivor_size):
            selected = self.selection.select(candidates)
            survivors.add_individual(selected.copy())
            candidates.individuals.remove(selected)
        return survivors

    def next_generation(self):
        new_population = Population(self.population_size, self.population.chromosome_length)

        survivors = self.select_survivors()
        for individual in survivors.individuals:
            new_population.add_individual(individual.copy())

        while len(new_population.individuals) < self.population_size:
            # Apenas os sobreviventes participam da reprodução.
            parent1 = random.choice(survivors.individuals)
            parent2 = random.choice(survivors.individuals)

            child1, child2 = self.crossover.execute(parent1, parent2)

            self.mutation.mutate(child1)
            new_population.add_individual(child1)
            if len(new_population.individuals) < self.population_size:
                self.mutation.mutate(child2)
                new_population.add_individual(child2)

        self.population = new_population

    def print_results(self):
        print(f"population size: {self.population_size}")
        print("initial population:")
        for index, individual in enumerate(self.initial_population, start=1):
            print(f"  {index}: {individual.chromosome} | cost: {individual.cost}")
        print("final population:")
        for index, individual in enumerate(self.population.individuals, start=1):
            print(f"  {index}: {individual.chromosome} | cost: {individual.cost}")
        print(f"generation size: {self.generation_size}")
        print(f"cities: {len(self.problem.cities)}")
        print(f"best cost: {self.best_individual.cost}")
        print(f"best route: {self.best_individual.chromosome}")

    def run(self) -> list[int]:
        self.initialize()
        self.evaluate()
        # Preserva a população inicial, com seus custos, para a exibição final.
        self.initial_population = [individual.copy() for individual in self.population.individuals]

        for generation in range(self.generation_size):
            should_stop = self.stagnation_criteria.verify(self.best_individual.cost)
            if should_stop:
                print(f"Stopping at generation {generation} due to stagnation.")
                break

            self.next_generation()
            self.evaluate()

        self.print_results()
        return self.best_individual.chromosome.copy()
