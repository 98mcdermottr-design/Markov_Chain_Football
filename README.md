# Markov_Chain_Football
Series of Markov Chains in Python to analyse football matches.

--- 

# Markov_Chain_Football_Simple.py

In this Python script I set out a simple Markov chain in action, used to determine the outcome of a football game between Manchester United and Liverpool, or a series of football games between Manchester United and Liverpool.

A Markov chain is a series of events, whereby the probability of each event is only dependent on the outcome of the previous event.

So in implementing this in python, we must first set out our conditional probabilities, in our case, it is the probability of Manchester United winning given the previous result was a Manchester United win, the probabilities of Liverpool winning given the previous result was a Manchester United win, etc.

Once we have this probability matrix made up, note it can be made up in the format of a pandas dataframe or a numpy array, in this version we start off with a pandas dataframe and then we convert it into a numpy array. But once we have this setup, we then select the first outcome completely at random, using np.random.choice. After we have our first result, each sequential result depends on our conditional probabilities. So with the pandas dataframe we use the previous result to find the associated conditional probabilities, and then reandomly select the next outcome considering these conditional probabilities. Then a loop can be ran to see what the outcome of multiple sequential games will be.

With the conditional probability matrix, we can just use a vector to represent the result of the first game, and then dot product the vector and the probability matrix to find the result probabilities for the next game. This can be done over and over again to find the probabilities for the 3rd, 4th, 5th, 6th, etc. game. After a large number of games we eventually arrive on a steady state probability matrix, or the stationary distribution which represents the long term probabilities of a Manchester United win, a Liverpool win, and q draw, independent of the starting condition.

---

# Markov_Chain_Football_InGameEvents.py

Same idea as the above, and same concepts applied, but now we are introducing a larger conditional probability matrix that we have imported from excel, in which we are projecting the sequence of events in a game, as well as the final result.

# Markov_Chain_Football_Multiple_Games.py

Same as the above, but with a small extension at the end to run a Monte Carlo simulation, to determine what the expected outcome from a premier league season would be.

So we have a loop in the code "for j in range(38)", this just takes the results of each game, based on the coniditional probabilities we have set out for in game events, and then repeats this process 38 times to see what the result of the season would look like.

Then we simply run this process 100 times and divide the season results by 100 to find out what our expected season result would be if we played the season 100 times over.

---

# Markov_Chain_Football_Multiple_Eig.py

As mentioned previously, doing the dot product of the transition (or stochastic) matrix with itself multiple times over, then you eventually find the long term probabilities.

But another way to find the long term probabilities is by finding the eigenvector, whose eigenvalue is equal to 1.

Every stochastic matrix has an eigenvalue equal to 1 for one of its eigenvectors, while all the other eigenvalues are less than 1 (this applies to normal, well-behaved stochastic matrices). This means that after multiple transitions the other probablities in the matrix collapse, and all you are left with are the probabilities in the eigenvector with eigenvalue = 1. Hence, if we find the eigenvalue with the eigenvector equal to (or very close to) 1, and then normalise this eigenvector, we've found the long-term probabilities, or the stationary distribution.

We find the eigenvectors and eigenvalues of the stochastic matrix using the function np.linalg.eig, and then find the eigenvector whose eigenvalue is close to 1 using the function np.isclose(eigvals, 1). From there we just normalise the eigencector, and the output of this is our long-term probabilities.
