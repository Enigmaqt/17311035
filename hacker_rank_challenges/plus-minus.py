#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    otric=0
    poloj=0
    nula=0
    for i in range(len(arr)):
        if(arr[i]>0):
            poloj+=1
        elif(arr[i]<0):
            otric+=1
        elif(arr[i]==0):
            nula+=1
    print(poloj/len(arr))
    print(otric/len(arr))
    print(nula/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)