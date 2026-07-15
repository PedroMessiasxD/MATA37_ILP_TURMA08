#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beadOrnaments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY b as parameter.
#

def beadOrnaments(b):
    MOD = 10**9 + 7
    N = len(b)
    
    if N == 1:
        if b[0] == 1:
            return 1
        return pow(b[0], b[0] - 2, MOD)
    
    S = sum(b)
    
    resultado = pow(S, N - 2, MOD)
    
    for x in b:
        resultado = (resultado * pow(x, x - 1, MOD)) % MOD
        
    return resultado
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        b_count = int(input().strip())

        b = list(map(int, input().rstrip().split()))

        result = beadOrnaments(b)

        fptr.write(str(result) + '\n')

    fptr.close()
