from scipy.io import loadmat

from genetic.selection.tournament_selection import TournamentSelection
from models.city import City
from problem.tsp import TSP
from genetic.genetic_algorithm import GA
from visualization.plot import plot_route


def load_cities() -> list[City]:
    data = loadmat("data/cities.mat")

    x = data["x"].flatten()
    y = data["y"].flatten()

    return [
        City(float(xi), float(yi))
        for xi, yi in zip(x, y)
    ]
        
if __name__ == "__main__":
    cities = load_cities()
    
    tsp = TSP(cities)
    
    ga = GA(
        problem=tsp, 
        population_size=1000, 
        generation_size=1000,
        elite_size=5,
        selection=TournamentSelection(tournament_size=3)
    )
    
    best = ga.run()
    
    plot_route(tsp.cities, best)
    