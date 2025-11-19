import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

events_prob = pd.read_excel("Continuous Probabilities.xlsx", header = 0, index_col = 0)
# get your conditional probability matrix from excel
game_length = int(input("How many minutes is the game? "))
starting_position = input("Is your team tipping off?(YES/NO) ").strip().upper()
if starting_position == "YES":
    starting_position = events_prob.index[0]
    x = "PASS OWN HALF"
else:
    starting_position = events_prob.index[4]
    x = "STAY WITHOUT POSESSION"

def match_events(events_prob):
    events = []
    home_goals = 0
    away_goals = 0
    events.append(x)
    next_event = x
    while len(events) < game_length:
        next_event = np.random.choice(events_prob.index, p = events_prob.iloc[events_prob.index.get_loc(next_event)])
        # generate next result, by finding probabilities for latest result get_loc(result)
        events.append(next_event)
        if next_event == "SCORE GOAL":
            home_goals += 1
        elif next_event == "CONCEDE GOAL":
            away_goals += 1
    return events, home_goals, away_goals

events, home_goals, away_goals = match_events(events_prob)

print(events)
if home_goals > away_goals:
    print(f"Home win, great {home_goals: .0f} - {away_goals: .0f} result")
elif home_goals < away_goals:
    print(f"Away win, disappointing {home_goals: .0f} - {away_goals: .0f} result")
else:
    print("Tie game")
