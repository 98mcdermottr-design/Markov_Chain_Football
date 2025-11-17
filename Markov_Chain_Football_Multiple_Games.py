import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

events_prob = pd.read_excel("Continuous Probabilities.xlsx", header = 0, index_col = 0)

def match_events(events_prob):
    x = np.random.choice(["PASS OWN HALF", "STAY WITHOUT POSESSION"])
    events = []
    home_goals = 0
    away_goals = 0
    events.append(x)
    next_event = x
    while len(events) < 90:
        next_event = np.random.choice(events_prob.index, p = events_prob.iloc[events_prob.index.get_loc(next_event)])
        events.append(next_event)
        if next_event == "SCORE GOAL":
            home_goals += 1
        elif next_event == "CONCEDE GOAL":
            away_goals += 1
    return home_goals, away_goals

wins = 0
losses = 0
draws = 0
N = 100
for i in range (N):
    season_wins = 0
    season_draws = 0
    season_losses = 0
    for j in range(38):
        home_goals, away_goals = match_events(events_prob)
        if home_goals > away_goals:
            season_wins += 1
        elif home_goals < away_goals:
            season_losses += 1
        else:
            season_draws += 1
    wins += season_wins
    losses += season_losses
    draws += season_draws

points = ((wins * 3) + draws) / N
win_percentage = wins/(38 * N)
avg_points = round(points / N, 0)
print(f"Season over, win percentage of {win_percentage: .1%}, and points of {points: .0f}")
