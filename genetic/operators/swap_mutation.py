import random

class SwapMutation:

    def validate(self, individual1: list[int], individual2: list[int]) -> bool:
        if len(individual1) != len(individual2):
            raise ValueError("Individuals must have the same length.")
        if set(individual1) != set(individual2):
            raise ValueError("Individuals must contain the same elements.")

        size = len(individual1)
        if size < 2:
            raise ValueError("Individuals must have at least two elements for mutation.")

        return True

    def mutate(
        self,
        individual1: list[int],
        individual2: list[int]
     ) -> tuple[list[int], list[int]]:
        self.validate(individual1, individual2)

        size = len(individual1)

        mutant1 = individual1.copy()
        mutant2 = individual2.copy()

        position = random.randrange(size)

        gene1 = individual1[position]
        gene2 = individual2[position]

        # identical genes: swapping changes nothing
        if gene1 == gene2:
            return mutant1, mutant2

        # swap genes
        mutant1[position] = gene2
        mutant2[position] = gene1

        # repair duplicates with a single mapping step (no loop):
        # mutant1 now has gene2 twice and lacks gene1, so the other
        # occurrence of gene2 receives gene1. Same logic for mutant2.
        self._replace_other_occurrence(mutant1, position, gene2, gene1)
        self._replace_other_occurrence(mutant2, position, gene1, gene2)

        return mutant1, mutant2

    @staticmethod
    def _replace_other_occurrence(
        chromosome: list[int],
        skip_position: int,
        old_gene: int,
        new_gene: int
    ) -> None:
        for i, gene in enumerate(chromosome):
            if i != skip_position and gene == old_gene:
                chromosome[i] = new_gene
                return
