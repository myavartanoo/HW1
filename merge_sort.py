import numpy as np
import math
from data_loader import loader
import argparse
import time

def Merge_sort(A,p,r):
    if p < r:
        q = int(math.floor((p+r)/2))

        Merge_sort(A,p,q)
        Merge_sort(A,q+1,r)
        Merge(A,p,q,r)


def Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = A[p:p+n1].copy()
    R = A[q+1:q+1+n2].copy()

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1


    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge_sort')


    parser.add_argument('-d', '--data', type=str, nargs='?', default='unknown_data',
        help='Please chose the dataset: -d almostsorted_10k')


    args = parser.parse_args()

    almostsorted_10k, random_10k, almostsorted_50k, random_50k = loader()
    data = args.data
    if data == 'unknown_data':
        data = input('Enter data type from  almostsorted_10k, random_10k, almostsorted_50k, random_50k : ')

    Time = np.zeros(100)
    print ('The input array is:')
    print (data)
    for n in range(100):
        sorted = data.copy()
        start = time.time()
        Merge_sort(sorted,0,np.size(sorted)-1)
        end = time.time()
        Time[n] = end-start
    print ('The sorted array is:')
    print (sorted)
    print ('The average time is: %.8f' % np.mean(Time))
    print ('The minimum time is: %.8f' % np.min(Time))
    print ('The maximum time is: %.8f' % np.max(Time))




