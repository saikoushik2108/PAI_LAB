import numpy as np

states = ["Rainy", "Sunny"]
obs_map = {"walk": 0, "shop": 1, "clean": 2}

pi = np.array([0.6, 0.4])

A = np.array([[0.7, 0.3],
              [0.4, 0.6]])

B = np.array([[0.1, 0.4, 0.5],
              [0.6, 0.3, 0.1]])

O = [obs_map[o] for o in ["walk", "shop", "clean"]]

def forward(O):
    T, N = len(O), len(pi)
    f = np.zeros((T, N))

    f[0] = pi * B[:, O[0]]

    for t in range(1, T):
        for j in range(N):
            f[t, j] = np.sum(f[t-1] * A[:, j]) * B[j, O[t]]

    return np.sum(f[-1])

print("Probability of observation sequence:",forward(O))