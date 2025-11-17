import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

mc_probs = {"Manu Win": [0.25, 0.25, 0.5],
                "Liverpool Win": [0.1, 0.75, 0.15],
                "Draw": [1/3, 1/3, 1/3]}

mc = pd.DataFrame(data = mc_probs, index = ["Manu Win", "Liverpool Win", "Draw"])
mc.to_excel("Probability Table.xlsx")

outcomes = []
outcomes.append(mc.index[0])
# sets first game as Manu win
result = np.random.choice(mc.index, p = mc.iloc[0])
# starting as Manu win, use those probabilities iloc[0], then choose the result of the next game
outcomes.append(result)
# add this next result to the list
while len(outcomes) < 25:
    result = np.random.choice(mc.index, p = mc.iloc[mc.index.get_loc(result)])
    # generate next result, by finding probabilities for latest result get_loc(result)
    outcomes.append(result)
# do it 25 times
print(outcomes)

mc_array = mc.to_numpy()
#instead of pandas have it in array

def matrix_power(matrix, power):
    if power == 0:
        return np.identity(len(matrix))
    elif power == 1:
        return matrix
    else:
        return np.dot(matrix, matrix_power(matrix, power - 1))
# apply the transition matrix multiple times to eventually find the steady state probabilities


for i in range (1, 10):
    print(f"\n", matrix_power(mc_array, i))

initial_dist = np.asarray([0, 0, 1])

print("\n", np.dot(initial_dist, matrix_power(mc_array, 2)))
