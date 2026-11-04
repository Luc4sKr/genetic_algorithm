from scipy.io import loadmat

from models.city import City


class CityLoader:
    
    @staticmethod
    def load(path: str) -> list[City]:
        data = loadmat(path)

        x = data["x"].flatten()
        y = data["y"].flatten()

        return [
            City(float(xi), float(yi))
            for xi, yi in zip(x, y)
        ]