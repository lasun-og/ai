import heapq

start = (1, 2, 3, 5, 0, 6, 4, 7, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
moves = [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]


def heuristic(puzzle):
    distance = 0
    for place, tile in enumerate(puzzle):
        if tile != 0:
            goal_place = tile - 1
            distance += abs(place // 3 - goal_place // 3)
            distance += abs(place % 3 - goal_place % 3)
    return distance


def solve():
    queue = [(heuristic(start), 0, start, [])]
    best_cost = {start: 0}

    while queue:
        _, cost, puzzle, path = heapq.heappop(queue)
        if puzzle == goal:
            return path
        if cost > best_cost[puzzle]:
            continue

        blank = puzzle.index(0)
        row, col = blank // 3, blank % 3
        for action, row_change, col_change in moves:
            new_row = row + row_change
            new_col = col + col_change
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                next_blank = new_row * 3 + new_col
                next_puzzle = list(puzzle)
                next_puzzle[blank], next_puzzle[next_blank] = (
                    next_puzzle[next_blank], next_puzzle[blank]
                )
                next_puzzle = tuple(next_puzzle)
                next_cost = cost + 1
                if next_cost < best_cost.get(next_puzzle, float("inf")):
                    best_cost[next_puzzle] = next_cost
                    next_path = path + [action]
                    heapq.heappush(
                        queue,
                        (next_cost + heuristic(next_puzzle), next_cost,
                         next_puzzle, next_path)
                    )
    return None


def show(puzzle):
    for row in range(0, 9, 3):
        print(puzzle[row:row + 3])


path = solve()
print("AI-3: 8 Puzzle")
print("Starting puzzle:")
show(start)

if path is None:
    print("No solution found.")
else:
    print("Moves:")
    print(path)
    print("Final puzzle:")
    show(goal)
    print("Total moves:", len(path))
