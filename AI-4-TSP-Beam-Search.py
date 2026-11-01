from math import hypot

cities = {
    "A": (0, 0),
    "B": (2, 1),
    "C": (5, 2),
    "D": (6, 5),
    "E": (3, 6)
}
beam_width = 3


def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return hypot(x2 - x1, y2 - y1)


paths = [(["A"], 0)]
while len(paths[0][0]) < len(cities):
    new_paths = []
    for path, cost in paths:
        for city in cities:
            if city not in path:
                new_path = path + [city]
                new_cost = cost + distance(path[-1], city)
                new_paths.append((new_path, new_cost))
    new_paths.sort(key=lambda item: item[1])
    paths = new_paths[:beam_width]

best_path = paths[0][0]
best_cost = paths[0][1] + distance(best_path[-1], "A")

print("AI-4: TSP using Local Beam Search")
print("Best tour:", " -> ".join(best_path + ["A"]))
print("Tour distance:", round(best_cost, 2))
