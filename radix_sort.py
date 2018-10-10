import numpy as np
import math
from data_loader import loader
import argparse
import time
from random import randint

def Counting_sort(A,k):
    C = np.zeros(k,dtype=int)
    s = np.size(A)
    for i in A:
        C[i] += 1
    total = 0
    D = np.zeros(k,dtype=int)
    for i in range(k):
        D[i] = total
        total += C[i]
    Output = np.zeros(s,dtype=int)
    indices = []
    for i in range(s):
        Output[D[A[i]]] = A[i]
        indices.append(D[A[i]])
        D[A[i]] += 1
    return Output, indices


def convert(A):
    max = np.max(A)

    count = 0
    while (max > 0):
        max = max // 10
        count = count + 1

    B = []
    for a in A:
        B.append(str(a).zfill(count))
    return np.array(B), count

def Radix_sort(A, count):
    for c in range(count):
        c = count-c-1

        arr = []
        for a in A:
            arr.append(int(a[c]))
        arr = np.array(arr)
        sorted, index = Counting_sort(arr,10)

        B = A.copy()
        for i in range(np.size(A)):
            B[index[i]] = A[i]
        A = B
    return np.array(A,dtype=int)





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
    data, count = convert(data)

    for n in range(100):
        start = time.time()
        sorted = Radix_sort(data,count)
        end = time.time()
        Time[n] = end-start
    print ('The sorted array is:')
    print (sorted)
    print ('The average time is: %.8f' % np.mean(Time))
    print ('The minimum time is: %.8f' % np.min(Time))
    print ('The maximum time is: %.8f' % np.max(Time))


