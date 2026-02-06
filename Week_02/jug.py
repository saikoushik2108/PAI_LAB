import heapq

def a_star_jug():
    start = (0,0)
    goal = int(input("Enter the goal:"))

    max_a = int (input("Enter jug A:"))
    max_b = int(input("Enter Jug B:"))

    def h(state):
        return abs(state[1] - goal)

    def get_neighbors(state):
        a, b = state
        moves = [
            (max_a, b),  # fill A
            (a, max_b),  # fill B
            (0, b),      # empty A
            (a, 0),      # empty B
            (a - min(a, max_b - b), b + min(a, max_b - b)),  # A -> B
            (a + min(b, max_a - a), b - min(b, max_a - a))   # B -> A
        ]
        return moves

    open_set = [(h(start), 0, start, [])]
    visited = set()

    while open_set:
        f, g, state, path = heapq.heappop(open_set)
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state[1] == goal:
            return path
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(open_set, (g+1+h(neighbor), g+1, neighbor, path))

solution = a_star_jug()
print("Solution path:", solution)
