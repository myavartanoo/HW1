import numpy as np
import math
from data_loader import loader
import argparse
import time
import sys
sys.setrecursionlimit(20000)

def Selection_sort(A):
    n = np.size(A)
    for i in range(0,n-1):
        smallest = i
        for j in range(i+1,n):
            if A[j] < A[smallest]:
                smallest = j
        A[smallest], A[i] = A[i], A[smallest]
    return A



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge_sort')


    parser.add_argument('-d', '--data', type=str, nargs='?', default='unknown_data',
        help='Please chose the dataset: -d almostsorted_10k')


    args = parser.parse_args()

    almostsorted_10k, random_10k, almostsorted_50k, random_50k = loader()
    data = args.data
    if data == 'unknown_data':
        data = input('Enter data type from  almostsorted_10k, random_10k, almostsorted_50k, random_50k : ')

    Time = np.zeros(2)
    print ('The input array is:')
    print (data)
    for n in range(2):
        start = time.time()
        sorted = Selection_sort(data)
        end = time.time()
        Time[n] = end-start
    print ('The sorted array is:')
    print (sorted)
    print ('The average time is: %.8f' % np.mean(Time))
    print ('The minimum time is: %.8f' % np.min(Time))
    print ('The maximum time is: %.8f' % np.max(Time))