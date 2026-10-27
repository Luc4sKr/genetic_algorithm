import random

from genetic.individual import Individual

class CycleCrossover:
    """Crossover Cycle (CX), que preserva permutações válidas.

    Escolhe uma posição inicial e identifica o ciclo de posições induzido
    pelos dois pais. Um filho recebe os genes desse ciclo do primeiro pai e
    as demais posições do segundo; o outro filho faz o inverso. Assim, cada
    cidade aparece exatamente uma vez em cada descendente.
    """

    def execute(self, parent_a: Individual, parent_b: Individual) -> tuple[Individual, Individual]:
        genes_a = parent_a.chromosome
        genes_b = parent_b.chromosome
        if len(genes_a) != len(genes_b) or set(genes_a) != set(genes_b):
            raise ValueError("Os pais precisam conter a mesma coleção de cidades.")

        length = len(genes_a)
        start = random.randrange(length)
        cycle_positions: set[int] = set()
        position = start

        # Segue o ciclo de posições conforme os valores do segundo pai.
        while position not in cycle_positions:
            cycle_positions.add(position)
            gene_from_b = genes_b[position]
            position = genes_a.index(gene_from_b)

        child_a: list[int] = []
        child_b: list[int] = []
        for index in range(length):
            if index in cycle_positions:
                child_a.append(genes_a[index])
                child_b.append(genes_b[index])
            else:
                child_a.append(genes_b[index])
                child_b.append(genes_a[index])

        return Individual(child_a), Individual(child_b)