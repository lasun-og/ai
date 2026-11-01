from collections import deque

grid = [
    "S....",
    ".##..",
    "...#.",
    ".#...",
    "....G"
]
directions = [("Down", 1, 0), ("Right", 0, 1),
              ("Up", -1, 0), ("Left", 0, -1)]
start = (0, 0)
goal = (4, 4)
queue = deque([(start, [])])
visited = {start}
path = None

while queue:
    position, moves = queue.popleft()
    if position == goal:
        path = moves
        break

    row, col = position
    for name, row_change, col_change in directions:
        next_row = row + row_change
        next_col = col + col_change
        next_position = (next_row, next_col)
        if (0 <= next_row < len(grid) and
                0 <= next_col < len(grid[0]) and
                grid[next_row][next_col] != "#" and
                next_position not in visited):
            visited.add(next_position)
            queue.append((next_position, moves + [name]))

print("AI-5: Robot Path using BFS")
for line in grid:
    print(line)

if path is None:
    print("No path found.")
else:
    print("Path:", path)
    print("Total moves:", len(path))
