import heapq

# Goal state
goal = (1,2,3,4,5,6,7,8,0)

# Possible moves for blank tile
moves = [(-3,'Up'), (3,'Down'), (-1,'Left'), (1,'Right')]

# Check if move is valid
def valid(pos, move):
    if move=='Left' and pos%3==0: return False
    if move=='Right' and pos%3==2: return False
    if move=='Up' and pos<3: return False
    if move=='Down' and pos>5: return False
    return True

# Manhattan distance heuristic
def heuristic(state):
    dist = 0
    for i, val in enumerate(state):
        if val==0: continue
        goal_pos = val-1
        dist += abs(i//3 - goal_pos//3) + abs(i%3 - goal_pos%3)
    return dist

# A* Search
def a_star(start):
    visited = set()
    heap = [(heuristic(start), 0, start, [])]  # (f=g+h, g, state, path)

    while heap:
        f, g, state, path = heapq.heappop(heap)
        if state==goal:
            print("Solution in", len(path), "moves:", path)
            return
        visited.add(state)
        zero = state.index(0)
        for move_val, move_name in moves:
            if not valid(zero, move_name): continue
            new_pos = zero + move_val
            new_state = list(state)
            new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
            new_state = tuple(new_state)
            if new_state not in visited:
                heapq.heappush(heap, (g+1+heuristic(new_state), g+1, new_state, path+[move_name]))
    print("No solution")

# --------- Main ---------
start = (1,2,3,4,0,6,7,5,8)
a_star(start)
