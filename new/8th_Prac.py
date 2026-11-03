
from collections import deque

def get_moves(state):
    moves = []
    n = len(state)

    for i in range(n):
        # A block can move only if it has no block above it
        if i < n - 1 and state[i + 1] == state[i]:
            continue

        # Move a clear block to the table
        new_state = list(state)
        new_state[i] = state[i]
        moves.append(tuple(new_state))

    return moves


def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        # Generate possible next states
        for next_state in get_valid_moves(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


def get_valid_moves(state):
    moves = []
    n = len(state)

    # state[i] tells which block supports block i
    for i in range(n):
        # Skip a block that has another block above it
        if i in state:
            continue

        for destination in range(-1, n):
            # -1 represents the table
            if destination == i or destination == state[i]:
                continue

            # A block cannot be placed on itself or on a block above it
            if destination != -1 and destination in state:
                continue

            new_state = list(state)
            new_state[i] = destination

            # Check that the move does not create a cycle
            current = destination
            valid = True

            while current != -1:
                if current == i:
                    valid = False
                    break
                current = new_state[current]

            if valid:
                moves.append(tuple(new_state))

    return moves


def display_state(state):
    for i, support in enumerate(state):
        if support == -1:
            print(chr(65 + i), "is on the table")
        else:
            print(chr(65 + i), "is on", chr(65 + support))


blocks = ["A", "B", "C"]

print("Enter the support of each block.")
print("Use -1 if the block is on the table.")
print("Example: -1 0 1 means A on table, B on A, C on B.")

start = tuple(map(int, input("Enter initial state (A B C): ").split()))
goal = tuple(map(int, input("Enter goal state (A B C): ").split()))

if len(start) != 3 or len(goal) != 3:
    print("Please enter exactly 3 values for each state.")
else:
    result = bfs(start, goal)

    if result is None:
        print("No plan found.")
    else:
        print("\nInitial State:")
        display_state(start)

        for step, state in enumerate(result, start=1):
            print("\nStep", step)
            display_state(state)

        print("\nGoal state reached in", len(result), "moves.")
