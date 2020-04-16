def rock_paper_scissors(n):
  # create inner function that passes a list instead of just a number
  # define list of length n
  if n < 1:
    return [[]]
  array = [[]]*(3**n)
  return rps(array)
  

  # define function which takes list as input
  # the base case is 'rock' 'paper' or 'scissors' being
  # appended to a "session"

  # The input to the base case is 1 item
  # the output to the base case is a list with 3 lists all prefixed
  # by the one item that came in. 
  # the base case is an empty list
  # if you get an empty list
  # return a list with 3 lists in it
  # you always have to return 1 list its just that the list contains 
  # other lists.
  # if you get 1 item, return 3 lists with 2 items each
  # if you get 2 items return 3 lists with 3 items each
  # The output is always going to be 3 lists with one more item than what came in
  
  # function outputs the final list

def rps(in_list):

  # Base case
  if len(in_list) == 3:
    return [['rock'],['paper'],['scissors']]

  a = len(in_list)//3
  third  = a 
  two_third = 2*a 
  # for i in len(in_list):
  #   if i < third:
  #     in_list[i] += 'rock'
  #   elif i< two_third:
  #     in_list[i] += 'paper'
  #   else:
  #     in_list[i] += 'scissors'

  part1 = in_list[:third]
  part2 = in_list[third:two_third]
  part3 = in_list[two_third:]

  rps1 = rps(part1)
  # You don't need dp because the pieces that 
  # are similar are literally repeated
  rps2 = rps1
  rps3 = rps1
  # rps2 = rps(part2)
  # rps3 = rps(part3)

  for i in range(len(rps1)):
    part1[i] = ['rock'] + rps1[i]
    part2[i] = ['paper'] + rps2[i]
    part3[i] = ['scissors'] + rps3[i]

  # this is how I finally got it. I got it working with 
  # a counter and by looping through elements in an array 
  # generated recursivley, and then I simplified the code
  # to what is written above.

  # counter = 0
  # for i in rps(part3):
  #   part3[i] = ['scissors'] + i
  #   counter += 1
  return part1 + part2 + part3
  
# print(rock_paper_scissors(5))

# Start with an emty list. if the length of the first element 
# = n 
# stop, return that list
# if it doesn't then 
# make a new list for every list where the new list contains
# 3 times the number of values as the first list. 

def rps2(n):
# output_len = 3**(n)
  # part_len = output_len//3

  part_len = 3**(n-1)

  part1 = [0]*int(part_len)
  part2 = [0]*int(part_len)
  part3 = [0]*int(part_len)

  if n < 1:
    return [[]]
  elif n == 1:
    return [['rock'],['paper'],['scissors']]
  else:
    base = rps2(n-1)
    # the length of base (previous) = 1/3 length of current

    for i in range(len(base)):
      part1[i] = ['rock'] + base[i]
      part2[i] = ['paper'] + base[i]
      part3[i] = ['scissors'] + base[i]
    
    return part1 + part2 + part3

# Now to preallocate all the memory:

def rps3(n):
  output_size = (3**n)
  offset = output_size//3
  output_arr = [0]*output_size

  if n < 1:
    return [[]]
  elif n == 1:
    return [['rock'],['paper'],['scissors']]
  else:
    base = rps3(n-1)
    
    # we can save some calculation here and just
    # loop by range(offset) cause the length of the "base"
    # case is going to be the same as the amount I'm offsetting by
    for i in range(len(base)):
      output_arr[i] = ['rock'] + base[i]
      output_arr[i+offset] = ['paper'] + base[i]
      output_arr[i+2*offset] = ['scissors'] + base[i]
    return output_arr
