#!/usr/bin/python

import sys

def making_change(amount, denominations, cache= None):
  # reference to current_max_denomination
  max_denom = denominations[-1]

  # cache setup
  if cache == None:
    cache = {}
    for i in denominations:
      cache[i] = [0]*(amount+1)
  
  # base cases 
  if denominations[-1] == 1:
    return 1
  elif amount < denominations[1]:
    return 1
  elif cache[max_denom][amount] != 0:
    return cache[max_denom][amount]

  # setting up variables for loop 
  max_iters = amount//max_denom
  new_denominations = denominations[:-1]
  count = 0

  # loop with recursion
  for i in range(max_iters+1):
    count += making_change(amount-(max_denom*i),new_denominations,cache)

  # assigning cache values/return
  cache[max_denom][amount] = count
  return count


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")