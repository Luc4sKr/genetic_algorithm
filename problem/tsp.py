from models.city import City

class TSP:
    def __init__(self, cities: list[City]):
        self.cities = cities
        
    def calculate_tour_distance(self, tour: list[int]) -> float:
        total_cost = 0.0
        for i in range(len(tour)):
            city_a = self.cities[tour[i]]
            city_b = self.cities[tour[(i + 1) % len(tour)]]
            total_cost += city_a.distance_to(city_b)
        return total_cost