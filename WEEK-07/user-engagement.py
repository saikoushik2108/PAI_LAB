from hmmlearn import hmm
import numpy as np

model = hmm.CategoricalHMM(n_components=3, n_iter=100)

model.startprob_ = np.array([0.5, 0.3, 0.2])

model.transmat_ = np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

model.emissionprob_ = np.array([
    [0.7, 0.3],
    [0.4, 0.6],
    [0.2, 0.8]
])

observations = np.array([[0], [1], [1], [0]])

hidden_states = model.predict(observations)

print("Predicted Hidden Engagement States:",hidden_states)
