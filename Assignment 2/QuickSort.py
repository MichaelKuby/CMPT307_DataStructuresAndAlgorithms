
#########################################################################
# Assignment 2 Question 4                                               *
#                                                                       #
# Implement the algorithm Randomized-Quicksort discussed in class       #
# and the variant of Randomized-Quicksort given in Question 3 by        #
# the same programming language (any language is OK) on the same        #
# computing platform. Report the running times of the two algorithms    #
# for sorting n numbers with n = 2^i × 1000, i = 0, 1, 2, 3, 4, 5.      #
#                                                                       #
# Give your suggestion on selecting k in practice (e.g., the k          #
# achieves the best running time in your implementation).               #
#                                                                       #
# You may not need to submit your program codes.                        #
#########################################################################
import random

def quicksort(A: list, p: int, r: int):
    """
    Sorts a list of integers
    A: list of integers
    p: low index of the array
    r: high index of the array
    """
    if p < r:
        q = randomized_partition(A, p, r)       
        quicksort(A, p, q-1)         # sort the high side
        quicksort(A, q+1, r)         # sort the low side

def randomized_partition(A: list, p: int, r: int):
    """
    A: list of integers
    p: low index of the array
    r: high index of the array
    """
    i = random.randint(p, r)
    A = swap(A, i, r)
    return partition(A, p, r)

def partition(A: list, p: int, r: int):
    """
    Rearranges the subarray A[p:r] in place, returning the index of
    the dividing point between the two sides of the partition.
    A: list of integers
    p: low index of the array
    r: high index of the array
    """
    pivot = A[r]
    low = p-1
    for j in range(p, r):
        if A[j] <= pivot:
            low += 1
            swap(A, low, j)
    swap(A, low+1, r)
    return (low + 1)

def quicksort_hybrid(A: list, p: int, r: int):
    """
    Sorts a list of integers by first quicksorting subarrays of length > k
    Then uses insertion sort to finish.
    A: list of integers
    p: low index of the array
    r: high index of the array
    k: Maximum size of subarray to ignore
    """
    _quicksort_hybrid(A, p, r)
    insertion_sort(A, p, r+1)


def _quicksort_hybrid(A: list, p: int, r: int):
    """
    Sorts a list of integers
    A: list of integers
    p: low index of the array
    r: high index of the array
    k: Maximum size of subarray to ignore
    """
    k= 75
    if p < r:
        q = randomized_partition_hybrid(A, p, r)
        if q-p > k:
            _quicksort_hybrid(A, p, q-1)         # sort the high side
        if r-q > k:
            _quicksort_hybrid(A, q+1, r)         # sort the low side
    
def randomized_partition_hybrid(A: list, p: int, r: int):
    """
    A: list of integers
    p: low index of the array
    r: high index of the array
    """
    i = random.randint(p, r)
    A = swap(A, i, r)
    return partition_hybrid(A, p, r)

def partition_hybrid(A: list, p: int, r: int):
    """
    Rearranges the subarray A[p:r] in place, returning the index of
    the dividing point between the two sides of the partition.
    A: list of integers
    p: low index of the array
    r: high index of the array
    """
    pivot = A[r]
    low = p-1

    for j in range(p, r):
        if A[j] <= pivot:
            low += 1
            swap(A, low, j)
    swap(A, low+1, r)
    return (low + 1)

def insertion_sort(A: list, m: int, n: int):
    """
    Sorts a list A of integers in place
    A: a list of integers
    m: start
    n: end
    """
    for i in range(m, n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

def swap (A: list, p: int, r: int):
    """
    Swaps A[p] with A[r]
    """
    A[p], A[r] = A[r], A[p]
    return A