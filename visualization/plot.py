import matplotlib.pyplot as plt

from models.city import City

def plot_route(cities: list[City], tour: list[int]) -> None:
    x = [cities[i].x for i in tour]
    y = [cities[i].y for i in tour]

    x.append(x[0])
    y.append(y[0])

    plt.figure(figsize=(9, 6))

    plt.plot(x, y, marker="o", linestyle="-")

    for i, city_index in enumerate(tour):
        city = cities[city_index]
        plt.annotate(
            str(city_index + 1),
            (city.x, city.y),
            xytext=(5, 5),
            textcoords="offset points"
        )

    plt.title("Melhor rota encontrada pelo Algoritmo Genético")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
