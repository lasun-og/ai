from collections import deque

world = ["S....", ".##..", "...#.", ".#...", "....G"]
moves = {"Down": (1, 0), "Right": (0, 1), "Up": (-1, 0), "Left": (0, -1)}
state = {"map": world, "position": (0, 0), "goal": (4, 4)}


def choose_path(state):
    queue = deque([(state["position"], [])])
    checked = {state["position"]}
    while queue:
        (row, col), path = queue.popleft()
        if (row, col) == state["goal"]:
            return path
        for action, (row_change, col_change) in moves.items():
            next_cell = (row + row_change, col + col_change)
            next_row, next_col = next_cell
            if (0 <= next_row < len(state["map"]) and
                    0 <= next_col < len(state["map"][0]) and
                    state["map"][next_row][next_col] != "#" and
                    next_cell not in checked):
                checked.add(next_cell)
                queue.append((next_cell, path + [action]))
    return []


path = choose_path(state)
print("AI-2: Grid Navigator")
print("S = Start, G = Goal, # = Obstacle")
for row in state["map"]:
    print(row)

if not path:
    print("No path found.")
else:
    print("Moves:")
    for action in path:
        row, col = state["position"]
        row_change, col_change = moves[action]
        state["position"] = (row + row_change, col + col_change)
        print(action, "->", state["position"])

    print("Goal reached!")
    print("Total moves:", len(path))
