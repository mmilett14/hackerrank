#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    min_sec = s[2:8]
    fmt = s[8:10]
    hour = int(s[0:2])


    if fmt == 'AM' and hour == 12:
        time = '00' + min_sec
        return time

    elif (fmt == 'AM' and hour > 0) or (fmt == 'PM' and hour == 12):
        time = s[0:8]
        return time

    elif fmt == 'PM' and hour > 0 and hour < 12:
        hour = hour + 12
        time = str(hour) + min_sec
        return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
