#!/usr/bin/python3

def best_score(D):
    top = 0
    winner = None
    for k, v in D.items():
        if v > top:
            top = v
            winner = k
    return winner
