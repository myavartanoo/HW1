import numpy as np
import math
from data_loader import loader
import argparse
import time
from random import randint

def Randomized_Quick_sort(A):
    s = np.size(A)
    if s >1:
        rand = randint(0,s-1)
        pivot = A[rand]
        A = np.delete(A,rand)
        L = A[np.where(A<pivot)]
        R = A[np.where(A>=pivot)]
        return np.hstack([Randomized_Quick_sort(L),pivot,Randomized_Quick_sort(R)])
    else:
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

    Time = np.zeros(100)
    print ('The input array is:')
    print (data)
    for n in range(100):
        start = time.time()
        sorted = Randomized_Quick_sort(data)
        end = time.time()
        Time[n] = end-start
    print ('The sorted array is:')
    print (sorted)
    print ('The average time is: %.8f' % np.mean(Time))
    print ('The minimum time is: %.8f' % np.min(Time))
    print ('The maximum time is: %.8f' % np.max(Time))