from collections import deque

def water_jug_bfs_path(a, b, target):
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    parent = {}  # to store the previous state

    while queue:
        x, y = queue.popleft()

        # Goal check
        if x == target or y == target:
            # Reconstruct the path
            path = [(x, y)]
            while (x, y) in parent:
                x, y = parent[(x, y)]
                path.append((x, y))
            path.reverse()
            print("\nSolution Path:")
            for px, py in path:
                print(px, py)
            print("Target reached!")
            return

        # Generate possible next states
        next_states = [
            (a, y),                          # Fill Jug A
            (x, b),                          # Fill Jug B
            (x - min(x, b - y), y + min(x, b - y)),  # Pour A -> B
            (x + min(y, a - x), y - min(y, a - x)),  # Pour B -> A
            (0, y),                          # Empty Jug A
            (x, 0)                           # Empty Jug B
        ]

        # Add unvisited states
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state] = (x, y)  # remember how we got here

    print("No solution exists")


# -------- Main Program --------
a = int(input("Jug A: "))
b = int(input("Jug B: "))
target = int(input("Target: "))

water_jug_bfs_path(a, b, target)

