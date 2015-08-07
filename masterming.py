#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from itertools import permutations
from random import choice

BASE = 8
DUPLICATES = False
LENGTH = 4
CARACTERS = [str(d) for d in range(BASE)]
UNIVERSE = list(permutations(CARACTERS, LENGTH))
OPORTUNITIES = 8

def get_hint(code, guess):
    assert len(code) == len(guess)
    full = sum(1  for c, g in zip(code, guess)  if c == g)
    partial = len(set(code) & set(guess)) - full
    return full, partial

def play():
    code = choice(UNIVERSE)
    for attempt in range(OPORTUNITIES):
        guess = raw_input("Guess (%d of %d): " % (attempt + 1, OPORTUNITIES))
        score = get_hint(code, guess)
        if score == (4, 0):
            print "You win!!!"
            break
        else:
            print score
    else:
        print "You loss, (losser)"
    print "The code was %s" % "".join(code)


def main():
    play()

if __name__ == "__main__":
    exit(main()) 
