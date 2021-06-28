#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_candle = 0
    max_candle_cnt = 0
    
    for i in range(0,len(candles)):
    
        if candles[i] > max_candle:
            max_candle_cnt = 1
            max_candle = candles[i]

        elif candles[i] == max_candle:
            max_candle_cnt += 1
            
    return max_candle_cnt
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
