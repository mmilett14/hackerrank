#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    i = 0
    j = 0
    k = n
    
    while i < n:
        
        while k > i + 1:
            print(" ")
            k -= 1
            
        while j <= i:
            print("#")
            j += 1
        
        print("")
        i += 1
        
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
