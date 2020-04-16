#!/usr/bin/python

import sys


# This one is actually iteration 3 (see rps3 in rps_trials.py)
# This iteration preallocates all the memory for the array upfront, and
# doesn't compose the output, but rather inserts all values into the
# preallocated memory space.

def rock_paper_scissors(n):
  output_size = (3**n)
  offset = output_size//3
  output_arr = [0]*output_size

  if n < 1:
    return [[]]
  elif n == 1:
    return [['rock'],['paper'],['scissors']]
  else:
    base = rock_paper_scissors(n-1)
    
    # we can save some calculation here and just
    # loop by range(offset) cause the length of the "base"
    # case is going to be the same as the amount I'm offsetting by
    for i in range(len(base)):
      output_arr[i] = ['rock'] + base[i]
      output_arr[i+offset] = ['paper'] + base[i]
      output_arr[i+2*offset] = ['scissors'] + base[i]
    return output_arr

rock_paper_scissors(2)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')