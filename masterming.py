#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from itertools import permutations, groupby
from random import choice
from copy import copy

BASE = 8
DUPLICATES = False
LENGTH = 4
CARACTERS = [str(d) for d in range(BASE)]
UNIVERSE = list(permutations(CARACTERS, LENGTH))
OPORTUNITIES = 8

def get_score(code, guess):
    assert len(code) == len(guess)
    full = sum(1  for c, g in zip(code, guess)  if c == g)
    partial = len(set(code) & set(guess)) - full
    return full, partial


def human_like(guess):
    score = (LENGTH - len(set(guess))) * 2
    prev = None
    for char in guess:
        if char == prev:
            score += 1
        if prev > char:
            score -= .5
    return score


def get_guess(universe):
    if universe == UNIVERSE: return "1356"
    minmax = "", "", ""
    for guess in universe:
        scores = (get_score(c, guess)  for c in universe)
        groups = [len(list(es))  for e, es in groupby(scores)]
        minmax = min(minmax, (max(groups), -human_like(guess), guess))
    print minmax
    return minmax[-1]


def play():
    print "Playing with:"
    print "base: %d (%s),  length: %d,   oportunities: %d" % (
        BASE, CARACTERS, LENGTH, OPORTUNITIES)
    print "special code: hint"
    code = choice(UNIVERSE)
    universe = copy(UNIVERSE)
    for attempt in range(OPORTUNITIES):
        print ""
        print "pos: % d" % len(universe)
        guess = raw_input("    Guess (%d of %d): " % (attempt + 1,
            OPORTUNITIES)).strip()
        if guess == "hint":
            guess = get_guess(universe)
            print "".join(guess) + " <- best play"

        score = get_score(code, guess)

        if score == (4, 0):
            print "You win!!!"
            break
        else:
            print "score", score
            universe = [p  for p in universe  if get_score(guess, p) == score]

    else:
        print "You loss, (losser)"
    print "The code was %s" % "".join(code)


def main():
    play()

if __name__ == "__main__":
    exit(main()) 
