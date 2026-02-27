# ------------------------------- 
# Import Libraries 
# -------------------------------
import matplotlib.pyplot as plt
import networkx as nx

# ------------------------------- 
# CSP Setup: 4 Variables, 4 Domains 
# -------------------------------
variables = ['A', 'B', 'C', 'D']
domains = {v: [1, 2, 3, 4] for v in variables}

# Constraint graph: connected variables cannot have same value
graph = {
    'A': ['B', 'C'],  # constraint 1 & 2
    'B': ['A', 'C', 'D'],  # constraint 3
    'C': ['A', 'B', 'D'],  # constraint 4
    'D': ['B', 'C']
}

# ------------------------------- 
# Function: Check if assignment is valid 
# -------------------------------
def is_valid(var, val, assignment):
    for neighbor in graph[var]:
        if assignment.get(neighbor) == val:
            return False
    return True

# ------------------------------- 
# Backtracking CSP Solver 
# -------------------------------
def backtrack(assignment={}):
    if len(assignment) == len(variables):
        return assignment
    var = next(v for v in variables if v not in assignment)
    for val in domains[var]:
        if is_valid(var, val, assignment):
            assignment[var] = val
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]
    return None

# ------------------------------- 
# Solve CSP 
# -------------------------------
solution = backtrack()
print("CSP Solution:")
for var, val in solution.items():
    print(f"{var} → {val}")

# ------------------------------- 
# Create Graph with Solution 
# -------------------------------
G = nx.Graph()
for var, neighbors in graph.items():
    for neigh in neighbors:
        G.add_edge(var, neigh)

# Node labels = variable + assigned value
node_labels = {var: f"{var}={solution[var]}" for var in variables}

# Draw graph
pos = nx.spring_layout(G, seed=42)  # fixed layout for reproducibility
nx.draw(G, pos, with_labels=True, labels=node_labels,
        node_color='lightblue', node_size=2000,
        font_size=14, font_weight='bold')
plt.title("CSP Solution Graph (4 Variables)")
plt.show()