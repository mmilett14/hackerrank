#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_sum = sum(arr)
    max_sum = sum(arr[0:3])
    
    for i in range(0, len(arr)):
        current_sum = sum(arr) - arr[i]
        
        if current_sum < min_sum:
            min_sum = current_sum
        
        if current_sum > max_sum:
            max_sum = current_sum
    
    print(min_sum, max_sum)
        
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
