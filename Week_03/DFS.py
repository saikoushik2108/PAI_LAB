def water_jug_dfs_path(a, b, target):
    visited = set()
    path = []

    def dfs(x, y):
        if (x, y) in visited:
            return False

        visited.add((x, y))
        path.append((x, y))

        if x == target or y == target:
            # Goal reached, print path
            print("\nSolution Path:")
            for px, py in path:
                print(px, py)
            print("Target reached!")
            return True

        # Possible next states (same fixed order)
        next_states = [
            (a, y),                          # Fill A
            (x, b),                          # Fill B
            (x - min(x, b - y), y + min(x, b - y)),  # Pour A -> B
            (x + min(y, a - x), y - min(y, a - x)),  # Pour B -> A
            (0, y),                          # Empty A
            (x, 0)                           # Empty B
        ]

        for state in next_states:
            if dfs(*state):
                return True  # stop at first solution

        path.pop()  # backtrack
        return False

    if not dfs(0, 0):
        print("No solution exists")


# -------- Main Program --------
a = int(input("Jug A: "))
b = int(input("Jug B: "))
target = int(input("Target: "))

water_jug_dfs_path(a, b, target)
