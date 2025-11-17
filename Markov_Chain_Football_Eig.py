import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

mc_array = np.array([[0.25, 0.25, 0.5],
                [0.1, 0.75, 0.15],
                [1/3, 1/3, 1/3]])

def matrix_power(matrix, power):
    if power == 0:
        return np.identity(len(matrix))
    elif power == 1:
        return matrix
    else:
        return np.dot(matrix, matrix_power(matrix, power - 1))
# apply the transition matrix multiple times to eventually find the steady state probabilities
approx_distribution = matrix_power(mc_array, 100)
approx_distribution = approx_distribution[0]

eigvals, eigvecs = np.linalg.eig(mc_array.T)
#calculate the eigenvalues and the eigenvectors of the probability matrix

stationary = eigvecs[:, np.isclose(eigvals, 1)]
# every stochastic matrix has an eigenvalue equal to 1 for one of its eigenvectors, while all the other eigenvalues are less than 1 (there are exceptions)
# this means that after multiple transitions the other probablities in the matrix collapse, and all you are left with
# are the probabilities in the eigenvector with eigenvalue = 1
stationary = stationary[:,0]
stationary = stationary / stationary.sum()
# normalize to sum to 1, to have actual probablities

print("Approximate distribution:", approx_distribution.real)
print("Stationary distribution:", stationary.real)

manu_long = stationary[0]
liverpool_long = stationary[1]
draw = stationary[2]
print(f"\nIn the long-term Manu have a{manu_long: .0%} chance of winning, \nLiverpool have a{liverpool_long: .0%} chance of winning \nAnd there is a{draw: .0%} chance of a draw.")
