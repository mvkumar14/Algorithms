#!/usr/bin/python
from math import inf

import argparse

def find_max_profit(prices):
  # keep track of min price so far
  # keep track of max profit so far
  min_price = prices[0] # maybe inefficient I think python has an "infinity"
  max_profit = prices[1]-prices[0]
  min_price_index = 0
  max_profit_index = 0

  # you have to run the for loop skipping the firtst index or else
  # you would never allow for negative profit.
  for index,i in enumerate(prices[1:]):
    if i < min_price:
      min_price = i
      min_price_index = index
    else:
      current_profit = i-min_price
      if current_profit > max_profit:
        max_profit = current_profit
        max_profit_index = index
  print(f"You would get max profit ({max_profit}) if you bought at {prices[min_price_index]} and sold at {prices[max_profit_index]}")
  return max_profit
  
  # The more generic CS way:
def find_max_profit2(prices):
  for i in range(len(prices)):
    if i == 0 :
      pass
  return 0
  # check against current min
  # if lower  
    # replace current min (+ index for explination)
    # next iteration of loop ( there is no way you are making profit )
  # if higher
    # check max profit
    # if larger
      # save new max profit (+ index for explination)
      # next
    # if smaller
      # next

find_max_profit([100, 90, 80, 50, 20, 10])


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))