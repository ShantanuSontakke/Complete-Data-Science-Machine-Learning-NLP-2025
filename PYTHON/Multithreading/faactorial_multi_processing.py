'''
Real-world Example: Multiprocessing for CPu-bound tasks
Scenario: factorial Calculation
Factorial calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the worked across multiple 
CPU cores , improveing performance.

'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integers cnversion
sys.set_int_max_str_digits(100000)

# function to compute factorials of a given number 

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}") 
    return result

if __name__=="__main__":
    numbers=[5000,6000,8000]

    start_time=time.time()

    #create a pool of worker process
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)
    
    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time -   start_time} seconds")