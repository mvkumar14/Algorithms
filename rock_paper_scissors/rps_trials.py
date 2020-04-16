import time
from rps_iterations import rock_paper_scissors, rps2, rps3

# array of n values:

# this is the number of rounds
n_values = list(range(5,15))
function_dictionary = {'rps1':rock_paper_scissors,'rps2':rps2,'rps3':rps3}
# function_dictionary = {'rps3':rps3}

for fun in function_dictionary:
    print()
    print(fun)
    for i in n_values:
        start_time = time.time()
        function_dictionary[fun](i)
        end_time = time.time()
        duration =  end_time-start_time
        print(i, duration)
