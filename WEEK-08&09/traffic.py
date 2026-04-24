states = ["Low", "Medium", "High"]
actions = ["Short", "Medium", "Long"]
gamma = 0.9

# Reward based on traffic density
reward = {"Low": 10, "Medium": 5, "High": -10}
V = {s:0 for s in states}

# Iteratively update state values
for _ in range(20):
    for s in states:
        V[s] = max(reward[s] + gamma * V[s] for a in actions)

print("Optimal State Values for Traffic Control:", V)
