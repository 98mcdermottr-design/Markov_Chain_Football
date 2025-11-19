import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

mc_probs = {"Manu Win": [0.25, 0.1, 1/3],
                "Liverpool Win": [0.25, 0.75, 1/3],
                "Draw": [0.5, 0.15, 1/3]}

mc = pd.DataFrame(data = mc_probs, index = ["Manu Win", "Liverpool Win", "Draw"])
# creates pandas dataframe with coniditional probablities
mc.to_excel("Probability Table.xlsx")
# export the pandas dataframe to excel

outcomes = []
# empty list containing the outcome of each game
outcomes.append(np.random.choice(mc.index))
# randomly select the outcome of the first game
result = np.random.choice(mc.index, p = mc.iloc[0])
# starting as Manu win, use those probabilities iloc[0], then choose the result of the next game at random based on the
# probabilities in the row of Manu win
outcomes.append(result)
# add this next result to the list of outcomes
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
# loop to find the transition matrix from 1 to 10 games
# after 10 games we should have found the steady state probabilities or something very close to it

initial_dist = np.asarray([0, 0, 1])
# now all in matrix and vector format, the above sets the first result equal to a draw

print("\n", np.dot(initial_dist, matrix_power(mc_array, 2)))
# find the probabilities of the 2nd result, if the first result was a draw
