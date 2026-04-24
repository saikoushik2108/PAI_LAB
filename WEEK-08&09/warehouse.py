states = ["Idle", "Working"]
actions = ["Work", "Charge"]
gamma = 0.9

# Initialize policy & state values
policy = {s: "Work" for s in states}
V = {s: 0 for s in states}

# Policy iteration loop
for _ in range(10):
    # Policy evaluation
    for s in states:
        V[s] = 5 + gamma * V[s]
    # Policy improvement
    for s in states:
        policy[s] = "Work" if V[s] > 2 else "Charge"
print("Optimal Warehouse Robot Policy:", policy)
