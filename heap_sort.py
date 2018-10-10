import numpy as np
import math
from data_loader import loader
import argparse
import time
from random import randint


def Max_Heapify(A, heap_size, i):
    L = 2 * i + 1
    R = 2 * i + 2
    largest = i
    if L < heap_size and A[L] > A[largest]:
        largest = L
    if R < heap_size and A[R] > A[largest]:
        largest = R
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, heap_size, largest)

def Build_Heap(A,heap_size):
    for i in range((heap_size/2),-1,-1):
        Max_Heapify(A,heap_size, i)
    return A

def Heap_sort(A):
    heap_size = np.size(A)
    heaped = Build_Heap(A,heap_size)
    for i in range(heap_size-1,0,-1):
        heaped[0], heaped[i] = heaped[i], heaped[0]
        heap_size -= 1
        Max_Heapify(A, heap_size, 0)
    return heaped




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
        sorted = Heap_sort(data)
        end = time.time()
        Time[n] = end-start
    print ('The sorted array is:')
    print (sorted)
    print ('The average time is: %.8f' % np.mean(Time))
    print ('The minimum time is: %.8f' % np.min(Time))
    print ('The maximum time is: %.8f' % np.max(Time))