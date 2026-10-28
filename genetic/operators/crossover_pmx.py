import random

from genetic.individual import Individual

class CrossoverPMX:
    def execute(
        self, 
        parent1: Individual, 
        parent2: Individual
    ) -> tuple[Individual, Individual]:
        self._validate_parents(parent1, parent2)
        
        size = len(parent1)
        
        start, end = sorted(random.sample(range(size), 2))
        
        child1 = self._create_child(
            parent1,
            parent2,
            start,
            end,
        )

        child2 = self._create_child(
            parent2,
            parent1,
            start,
            end,
        )

        return child1, child2
    
    @staticmethod
    def _validate_parents(
        parent1: Individual,
        parent2: Individual,
    ) -> None:
        if len(parent1.chromosome) != len(parent2.chromosome):
            raise ValueError(
                "Os pais devem ter o mesmo tamanho."
            )

        if len(parent1.chromosome) < 2:
            raise ValueError(
                "Os pais devem ter pelo menos dois genes."
            )

        if len(set(parent1.chromosome)) != len(parent1.chromosome):
            raise ValueError(
                "O primeiro pai possui genes duplicados."
            )

        if len(set(parent2.chromosome)) != len(parent2.chromosome):
            raise ValueError(
                "O segundo pai possui genes duplicados."
            )

        if set(parent1.chromosome) != set(parent2.chromosome):
            raise ValueError(
                "Os pais devem conter os mesmos genes."
            )
    
    def _create_child(
        self,
        parent1: Individual,
        parent2: Individual,
        start: int,
        end: int,
    ) -> Individual:
        size = len(parent1.chromosome)
        child = [None] * size

        child[start:end + 1] = parent1.chromosome[start:end + 1]

        for i in range(start, end + 1):
            gene = parent2.chromosome[i]

            if gene in child:
                continue

            position = i

            while start <= position <= end:
                mapped_gene = parent1.chromosome[position]
                position = parent2.chromosome.index(mapped_gene)

            child[position] = gene

        for i in range(size):
            if child[i] is None:
                child[i] = parent2.chromosome[i]

        return Individual(chromosome=child)