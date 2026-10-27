
class StagnationCriteria:
    def __init__(self, stagnation_limit: int):
        self.stagnation_limit = stagnation_limit
        self.best_fitness_history = []
        self.stagnation_counter = 0

    def verify(self, best_fitness: float) -> bool:
        if (
            not self.best_fitness_history
            or best_fitness < self.best_fitness_history[-1]
        ):
            self.best_fitness_history.append(best_fitness)
            self.stagnation_counter = 0
        else:
            self.stagnation_counter += 1

        print(
            f"Stagnation counter: "
            f"{self.stagnation_counter}/{self.stagnation_limit}"
        )

        return self.stagnation_counter >= self.stagnation_limit
