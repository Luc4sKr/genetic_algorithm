import numpy as np

from models.city import City


class Problem:
    def __init__(self, cities: list[City]):
        self.cities = cities

        # coordenadas em arrays para operar de forma vetorizada.
        coords = np.array([(c.x, c.y) for c in cities], dtype=np.float64)
        self._coords = coords

        # matriz de distâncias NxN pré-computada
        diff = coords[:, np.newaxis, :] - coords[np.newaxis, :, :]
        self._distance_matrix = np.sqrt(np.einsum("ijk,ijk->ij", diff, diff))

        self._matrix = self._distance_matrix.tolist()
    
    @property
    def distance_matrix(self) -> np.ndarray:
        """Matriz NxN de distâncias euclidianas entre cidades (pré-computada)."""
        return self._distance_matrix

    def distance(self, i: int, j: int) -> float:
        """Distância O(1) entre as cidades i e j"""
        return self._matrix[i][j]
    
    def evaluate(self, chromosome: list[int]) -> float:
        ...