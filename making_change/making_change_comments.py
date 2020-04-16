# Same as making_change just with more human readable comments

def making_change(amount, denominations, cache= None):
  max_denom = denominations[-1]

  if cache == None:
    cache = {}
    for i in denominations:
      cache[i] = [0]*(amount+1)
  
  # I have two base cases 

  # 1 is if the only denomination I have is 1s

  # 2 is if the amount is less than the second least 
  # denomination (generally)
  # or 5 cents if we are using us currency
  
  # you have to check in this order so you don't get an index
  # error
  
  if denominations[-1] == 1:
    return 1
  if amount < denominations[1]:
    return 1
  elif cache[max_denom][amount] != 0:
    return cache[max_denom][amount]

  # loop through all the amounts of max_denom 
  # currency you can use
  # for example making_change(50)
  # max_denom = 50
  # combos:
  # 0 half dollar + every combination of 51 cent
  # 1 half dollar + every combination of 1 cent

  max_iters = amount//max_denom
  new_denominations = denominations[:-1]

  count = 0
  for i in range(max_iters+1):
    count += making_change(amount-(max_denom*i),new_denominations,cache)

  # update the cache
  cache[max_denom][amount] = count

  # return count (up one level of recursion)
  return count