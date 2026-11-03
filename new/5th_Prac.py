
import heapq

# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal = state[i] - 1
            row1, col1 = i // 3, i % 3
            row2, col2 = goal // 3, goal % 3

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


# Display the puzzle
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# A* Search Algorithm
def solve(start):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            print("\nSolution found!")
            print("Steps required:", len(path) - 1)

            for step in path:
                display(step)

            return

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        moves = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)

                new_state[zero], new_state[new_zero] = (
                    new_state[new_zero], new_state[zero]
                )

                new_state = tuple(new_state)

                if new_state not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(new_state)

                    heapq.heappush(
                        pq, (new_f, new_g, new_state, path)
                    )

    print("No solution found.")


# Take input from the user
print("Enter the 8-Puzzle numbers row by row.")
print("Use 0 for the blank space.")

numbers = []

for i in range(3):
    row = list(map(int, input("Enter row " + str(i+1) + ": ").split()))
    numbers.extend(row)

if len(numbers) == 9 and sorted(numbers) == list(range(9)):
    solve(tuple(numbers))
else:
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
