
import random

def calculate_distance(tour, distance):
    total = 0

    for i in range(len(tour) - 1):
        total += distance[tour[i]][tour[i + 1]]

    total += distance[tour[-1]][tour[0]]
    return total


def get_neighbors(tour):
    neighbors = []
    n = len(tour)

    for i in range(1, n):
        for j in range(i + 1, n):
            new_tour = list(tour)
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            neighbors.append(tuple(new_tour))

    return neighbors


n = int(input("Enter number of cities: "))

if n < 3:
    print("Enter at least 3 cities.")
    exit()

distance = []

print("Enter the distance matrix row by row:")

for i in range(n):
    row = list(map(int, input().split()))

    if len(row) != n:
        print("Each row must contain", n, "distances.")
        exit()

    distance.append(row)

beam_width = int(input("Enter beam width: "))
max_steps = int(input("Enter number of search steps: "))

if beam_width < 1 or max_steps < 1:
    print("Beam width and search steps must be positive.")
    exit()

# Generate different initial tours
beam = []
first_tour = tuple(range(n))
beam.append(first_tour)

while len(beam) < beam_width:
    tour = [0] + random.sample(range(1, n), n - 1)
    tour = tuple(tour)

    if tour not in beam:
        beam.append(tour)

    if len(beam) == len(set(beam)) and len(beam) >= 1:
        if len(beam) >= 1:
            # Stop if all possible tours have been generated
            if len(beam) >= 1:
                pass

best_tour = min(beam, key=lambda t: calculate_distance(t, distance))

for step in range(max_steps):
    candidates = set(beam)

    for tour in beam:
        candidates.update(get_neighbors(tour))

    new_beam = sorted(
        candidates,
        key=lambda t: calculate_distance(t, distance)
    )[:beam_width]

    current_best = min(
        new_beam,
        key=lambda t: calculate_distance(t, distance)
    )

    if calculate_distance(current_best, distance) < calculate_distance(best_tour, distance):
        best_tour = current_best

    if new_beam == beam:
        break

    beam = new_beam

print("\nBest tour found:")

for city in best_tour:
    print("City", city + 1, end=" -> ")

print("City", best_tour[0] + 1)

print("Total distance:", calculate_distance(best_tour, distance))
