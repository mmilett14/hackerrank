#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total = len(arr)
    
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    
    answers = [round(pos/total, 6), round(neg/total, 6), round(zero/total, 6)]
    
    for i in range(0, len(answers)):
        print(answers[i])

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
