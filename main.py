from genetic.selection.roulette_selection import RouletteSelection
from genetic.stagnation_criteria import StagnationCriteria
from loaders.cities_loader import CityLoader
from problem.tsp import TSP
from genetic.genetic_algorithm import GA
from visualization.plot import plot_route

if __name__ == "__main__":
    cities = CityLoader.load("data/cities.mat")

    tsp = TSP(cities)

    ga = GA(
        problem=tsp,
        population_size=20,
        generation_size=10_000,
        survivor_size=10,  # Mantém os dez melhores; a roleta seleciona os pais.
        selection=RouletteSelection(),
        stagnation_criteria=StagnationCriteria(stagnation_limit=1000)
    )

    best = ga.run()

    plot_route(tsp.cities, best)
