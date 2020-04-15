#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n,cache=None):
  print(n)
  if cache is None:
    cache = [0]*(n+1)
  if n < 0:
    return 0
  elif n < 2:
    return 1
  elif cache[n] != 0:
    return cache[n]
  else:
    answer = eating_cookies(n-1,cache) + eating_cookies(n-2,cache) + eating_cookies(n-3,cache)
    cache[n] = answer
    return answer


# I want my recursive function to return:
# eating_cookies(n-1))
# that too can be written recursivley? So you can make the number
# of cookies you can eat at once a variable paramter.


# How many ways are there to eat 10 cookies?
# all the ways you can eat 9  cookies + eat 1 cookie
# + all the ways you can eat 8 cookies + 2 cookies
# + all the ways you can eat 7 cookies + 3 cookies


# this is the basis of the recursion for this problem
# The base case is 1 cookie. There is only 1 way to eat one cookie.

# the permuations, however are 

# in combinatorics its something like n choose 3? 

# Within each level 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')