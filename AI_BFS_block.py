from collections import deque

start = (("A", "C"), ("B",))
goal = (("C", "B", "A"),)


def bfs(start, goal):

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:

        state = queue.popleft()

        if state == goal:
            break

        for i in range(len(state)):

            if not state[i]:
                continue

            block = state[i][-1]

            # Remove the top block
            new_state = list(state)
            new_state[i] = new_state[i][:-1]

            source_removed = not new_state[i]

            if source_removed:
                new_state.pop(i)

            # Move block onto the table
            table_state = tuple(
                sorted(new_state + [(block,)])
            )

            if table_state not in visited:
                visited.add(table_state)
                parent[table_state] = state
                queue.append(table_state)

            # Move block onto another stack
            for j in range(len(new_state)):

                # Skip original stack only if it still exists
                if not source_removed and i == j:
                    continue

                updated = list(new_state)
                updated[j] = updated[j] + (block,)

                next_state = tuple(sorted(updated))

                if next_state not in visited:
                    visited.add(next_state)
                    parent[next_state] = state
                    queue.append(next_state)

    # Check if goal was reached
    if goal not in parent:
        return None

    # Reconstruct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path


path = bfs(start, goal)

if path:

    print("Shortest path:")

    for state in path:
        print(state)

    print("Minimum moves:", len(path) - 1)

else:
    print("No solution found.")
