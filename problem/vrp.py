from problem.problem import Problem
from models.city import City

class VRP(Problem):
    def __init__(self, cities: list[City], num_vehicles: int, vehicle_capacity: int):
        super().__init__(cities)
        self.num_vehicles = num_vehicles
        self.vehicle_capacity = vehicle_capacity

    def evaluate(self, chromosome: list[int]) -> float:
        # TODO: Implement the evaluation function for the VRP problem
        pass
    